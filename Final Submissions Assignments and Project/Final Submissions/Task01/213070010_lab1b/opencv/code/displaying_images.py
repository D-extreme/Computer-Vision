import cv2
import os
import argparse


def image_display(path):
    # List of path of images at the specified directly path
    images = os.listdir(path)

    # Initialization for the first image
    i = 0
    filename = os.path.join(path, images[i])
    image = cv2.imread(filename)  # Reading the image into a numpy array
    cv2.imshow("Display Window", image)  # Displaying the first image
    k = cv2.waitKey(0)
    while k != ord('e'):
        if k == ord('n'):
            if i < len(images) - 1:
                filename = os.path.join(path, images[i + 1])
                image = cv2.imread(filename)
                cv2.imshow("Display Window", image)  # Displaying the next image from the directory when 'n' is pressed
                k = cv2.waitKey(0)
                i += 1
            else:
                if i >= len(images) - 1:  # Counter reaches the end of the list, reinitialize i=-1 (Wrap around)
                    i = -1
                if i < -1:
                    i = len(images) - 1  # Counter reaches the beginning of the list i= len(images) - 1 (Wrap around)
        # Similar implementation of pressing 'p' as above
        if k == ord('p'):
            if i >= 0:
                i -= 1
                filename = os.path.join(path, images[i])
                image = cv2.imread(filename)
                cv2.imshow("Display Window", image)
                k = cv2.waitKey(0)
            else:
                if i > len(images) - 1:
                    i = 0
                if i < 0:
                    i = len(images) - 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, nargs='?')

    arguments = parser.parse_args()
    path_to_dir = arguments.path

    if path_to_dir is not None:
        image_display(path_to_dir)
    else:
        print("Invalid Path")
