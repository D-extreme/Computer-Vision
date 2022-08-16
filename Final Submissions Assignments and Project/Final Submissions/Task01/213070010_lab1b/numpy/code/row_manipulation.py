import numpy as np
import argparse


# Function for computing the NxN row matrix
def transformation_matrix(N):
    #  Creating an identity matrix of ceil(N/2)
    identity = np.identity(int(np.ceil(N / 2)))
    # Formatting the identity matrix by inserting zero vectors at desired indices using numpy.insert
    formatted_identity = np.insert(identity, np.arange(1, int(np.ceil(N // 2)) + 1), 0, axis=1)

    # If N=1, return [1]
    if N == 1:
        return np.array([1])
    if N % 2 == 0:  # N = even, circularly rotate the formatted matrix by 1 unit towards right
        temp_arr = np.roll(formatted_identity, 1, axis=1)
    else:  # N = odd, circularly rotate (N//2) tops rows the formatted matrix by 1 unit towards right
        temp_arr = np.roll(formatted_identity[0:(N // 2)], 1, axis=1)
    # Final output by concatenating the formatted identity matrix with the circularly shifted one along the rows
    final_arr = np.concatenate((formatted_identity, temp_arr), axis=0)
    return final_arr


# Function for cropping the array
def crop_array(arr_2d, offset_height, offset_width, target_height, target_width):
    new_arr = arr_2d[offset_height: target_height + offset_height, offset_width: offset_width + target_width]
    return new_arr


# Function for padding the array
def padded_array(arr_2d, pad_value, pad_width):
    arr = np.pad(arr_2d, pad_width=pad_width, mode='constant', constant_values=pad_value)
    return arr


# Function for concatenating the padded array with itself
def concatenated(arr_2d):
    arr = np.concatenate((arr_2d, arr_2d), axis=1)
    return arr


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--N', type=int, nargs='?')

    arguments = parser.parse_args()
    N_val = arguments.N
    if N_val is not None:
        trans_mat = transformation_matrix(N_val)
        print("Original array: \n", trans_mat)
        cropped_array = crop_array(trans_mat, 1, 1, 2, 2)
        print("Cropped array: \n", cropped_array)
        pad_array = padded_array(cropped_array, 0.5, 2)
        print("Padded array: \n", pad_array)
        concat_array = concatenated(pad_array)
        print("Concatenated array: shape = ", np.shape(concat_array), "\n", concat_array)
    else:
        print("Input not received")
