"""Loading, saving and displaying images."""
import sys

import cv2 as cv


"""Load an image from the specified path."""
def load_image(img_path, show_image=False):
    # ? check if the image path is valid
    if not img_path or not isinstance(img_path, str):
        sys.exit("Error: No image path provided.")

    img = cv.imread(img_path)

    # ? safely exit the program if the image cannot be loaded
    if img is None:
        sys.exit(f"Error: Unable to load image at {img_path}")

    if show_image:
        cv.imshow("Display window", img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    return img
