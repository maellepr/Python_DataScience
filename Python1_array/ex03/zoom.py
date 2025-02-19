from load_image import ft_load
import os
from PIL import Image
from numpy.typing import NDArray
import numpy as np
import matplotlib.pyplot as plt


def display(array: np.array):
    """
    Display the image.
    """
    plt.imshow(array, cmap='gray')
    plt.show()


def zoom(img: NDArray[np.uint8]):
    """
    Takes an image as input and returns a zoomed version of it,
    in black and white.

    -> NDArray is a multidimensional array type with elements of
    the same size and type. It is a generic type, so we should
    specify the type of the elements in the array.
    -> np.uint8 is an 8-bit unsigned integer type.

    img[100:500, 450:850] is zooming into a specific part of the image.
    The 1rst slice is for the height and the 2nd slice is for the width.
    [..., :3] is for extracting the RGB values of the image.
    .dot(0.2989, 0.5870, 0.1140) is for converting the RGB values to
    black and white.
    [..., np.newaxis] is for adding a new axis to the array to keep
    the grayscale image in a single-channel format.
    np.asarray(..., dtype=np.uint8) ensures the final output is still
    an np.uint8 array (as img are usually stored).
    """
    return np.asarray(
        img[100:500, 450:850][..., :3].dot(
            (0.2989, 0.5870, 0.1140)
        )[..., np.newaxis],
        dtype=np.uint8
    )


def main():
    """
    Open an image, load it as a numpy array, call the zoom function
    and display the zoomed image.
    """
    try:
        path = "animal.jpeg"
        if not os.path.exists(path):
            raise AssertionError("File not found.")
        img = Image.open(path)
        if img is None:
            raise AssertionError("Error in loading image.")
        img_array = ft_load(path)
        print(img_array)
        img_zoomed = zoom(img_array)

        print(f"New shape after slicing: {img_zoomed.shape}")
        print(img_zoomed)
        display(img_zoomed)

    except AssertionError as e:
        print("AssersionError:", e)


if __name__ == "__main__":
    main()
