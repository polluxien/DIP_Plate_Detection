"""Plate localization via edge detection and contour analysis."""
import cv2 as cv


def canny_edge_detection(img, show_image=False):
    edges = cv.Canny(img, 100, 200)

    if show_image:
        cv.imshow("Display window", edges)
        cv.waitKey(0)
        cv.destroyAllWindows()
    return edges
