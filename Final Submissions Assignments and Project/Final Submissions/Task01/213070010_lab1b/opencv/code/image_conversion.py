import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt


def normalization(image):
    max_val = np.max(image)
    min_val = np.min(image)
    norm_image = (image - min_val) / (max_val - min_val)
    return norm_image


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, nargs='?')

    arguments = parser.parse_args()
    path_to_image = arguments.path

    # Image in BGR
    image = cv2.imread(path_to_image)  # dtype is uint8
    normalized_image = normalization(image)

    # Image in RGB as matplotlib accepts in RGB format
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    normalized_image_rgb = normalization(image_rgb)  # Normalized Image

    # Plotting the figures using Matplotlib
    fig = plt.figure()
    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.subplot(1, 2, 2)
    plt.imshow(normalized_image_rgb)
    plt.title("Normalized Image")
    plt.show()

    plt.imsave('../results/original_plt.jpg', image_rgb)
    plt.imsave('../results/normalized_plt.jpg', normalized_image_rgb)

    cv2.imshow("Original Image", np.uint8(image))
    cv2.imshow("Normalized Image", np.uint8(255*normalized_image_rgb))
    cv2.moveWindow("Original Image", 400, 500)
    x, y, w, h = cv2.getWindowImageRect("Original Image")
    cv2.moveWindow("Normalized Image", x + w, 500)
    cv2.waitKey(0)

    cv2.imwrite('../results/original_cv2.jpg', np.uint8(image))
    cv2.imwrite('../results/normalized_cv2.jpg', np.uint8(255*normalized_image_rgb))
