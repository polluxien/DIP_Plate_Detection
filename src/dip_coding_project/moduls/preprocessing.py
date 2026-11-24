"""Preprocessing: color conversion, denoising, binarization."""
import cv2 as cv


"""Convert the image to grayscale."""
def grayscale_image(img, show_image=False):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    if show_image:
        cv.imshow("Display window", gray)
        cv.waitKey(0)
        cv.destroyAllWindows()
    return gray
