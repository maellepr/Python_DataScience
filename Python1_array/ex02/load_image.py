import os
from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    This function loads an image from a given path,
    print its format and its pixls content in RGB format
    and returns the image as a numpy array.
    """
    try:
        if not os.path.exists(path):
            raise AssertionError("File not found.")
        if not path.endswith((".jpg", ".jpeg")):
            raise AssertionError("File should be a jpg or jpeg")
        img = Image.open(path)
        img_array = np.array(img)
        print(f"The shape of image is: {img_array.shape}")
        return img_array
    except AssertionError as e:
        print("AssersionError:", e)
        return ""
    except Exception as e:
        print("Error:", e)
        return ""


def main():
    """
    Calls the ft_load function
    and does some testing.
    """
    path = "landscape.jpg"
    print(ft_load(path))


if __name__ == "__main__":
    main()
