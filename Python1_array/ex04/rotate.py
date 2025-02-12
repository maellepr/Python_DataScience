from load_image import ft_load
import os
from PIL import Image
from numpy.typing import NDArray
import numpy as np
import matplotlib.pyplot as plt


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


def rotate(img: NDArray[np.uint8], axes: tuple[int, ...]):
    # return np.asarray(
    #     img[100:500, 450:850][..., :3].dot(
    #         (0.2989, 0.5870, 0.1140)
    #     )[..., np.newaxis],
    #     dtype=np.uint8
    # )
    data = np.asarray(img)
    shape = img.shape
    rotated_shape = tuple(shape[i] for i in axes)
    img_rotated = np.zeros(rotated_shape, dtype=data.dtype)
    for index in np.ndindex(shape):
        index_rotated = tuple(index[i] for i in axes)
        img_rotated[index_rotated] = data[index]
    return img_rotated


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
       

        img_zoomed = zoom(img_array)
        print(f"The shape of image is: {img_zoomed.shape}")
        print(img_zoomed)

        img_rotated = rotate(img_zoomed, (1, 0, 2)).squeeze(axis=2)

        print(f"New shape after slicing: {img_rotated.shape}")

        print(img_rotated)

        plt.imshow(img_rotated, cmap='gray')
        plt.show()

    except AssertionError as e:
        print("AssersionError:", e)


if __name__ == "__main__":
    main()
