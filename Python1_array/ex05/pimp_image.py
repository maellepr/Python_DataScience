from load_image import ft_load
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def display(array: np.array):
    """
    Display the image.
    """
    plt.imshow(array, cmap='gray')
    plt.show()


def ft_grey(array: np.array):
    """
    Takes an image as input and returns a greyscale version of it.
    """
    return np.asarray(
        array.dot(
            (0.2989, 0.5870, 0.1140)
        ),
        dtype=np.uint8
    )


def ft_blue(array: np.array):
    """
    Takes an image as input and returns an image with only the blue channel.
    """
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            array[i, j, 0] = 0
            array[i, j, 1] = 0
    return array


def ft_green(array: np.array):
    """
    Takes an image as input and returns an image with only the green channel.
    """
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            array[i, j, 0] = 0
            array[i, j, 2] = 0
    return array


def ft_red(array: np.array):
    """
    Takes an image as input and returns an image with only the red channel.
    """
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            array[i, j, 1] = 0
            array[i, j, 2] = 0
    return array


def ft_invert(array: np.array):
    """
    Takes an image as input and returns an image with the colors inverted.
    """
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            for k in range(array.shape[2]):
                array[i, j, k] = 255 - array[i, j, k]
    return array


def main():
    """
    Open an image, load it as a numpy array, call the zoom function
    and display the zoomed image.
    """
    try:
        path = "landscape.jpg"
        if not os.path.exists(path):
            raise AssertionError("File not found.")
        img = Image.open(path)
        if img is None:
            raise AssertionError("Error in loading image.")
        img_array = ft_load(path)

        print(f"The shape of image is: {img_array.shape}")
        print(img_array)

        img_invert = ft_invert(img_array.copy())
        img_red = ft_red(img_array.copy())
        img_green = ft_green(img_array.copy())
        img_blue = ft_blue(img_array.copy())
        img_grey = ft_grey(img_array.copy())

        # print(f"New shape after inverting: {img_invert.shape}")
        # print(img_invert)
        display(img_invert)
        display(img_red)
        display(img_green)
        display(img_blue)
        display(img_grey)

    except AssertionError as e:
        print("AssersionError:", e)


if __name__ == "__main__":
    main()
