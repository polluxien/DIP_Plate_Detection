import cv2 as cv
import numpy as np
import sys

# 1. load the image
# 2. get rid of noises
# 3. convert to grayscale
# 4. image detection
#.   group plate
# 5. character segmentation
# 6. read the plate and return the text
#    show the image with the detected plate and the text on it

# think about involving machine learning to improve the accuracy of the plate detection and recognition process. 
# This could involve training a model on a dataset of license plates to better identify and read them, especially 
# in challenging conditions such as low light or occlusions.

def main():
    print("Initializing the application...")
    
    img = load_image("/Users/bennet/Desktop/Istanbul Uni/Digital Image Perocessing/dip_coding_project/sample/34469040.jpg", False)
    gray_img = grayscale_image(img, False)
    edges = canny_edge_detection(gray_img, True)

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

"""Convert the image to grayscale."""
def grayscale_image(img, show_image=False):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    if show_image:
        cv.imshow("Display window", gray)
        cv.waitKey(0)
        cv.destroyAllWindows()
    return gray

def canny_edge_detection(img, show_image=False):
    edges = cv.Canny(img, 100, 200)
    
    if show_image:
        cv.imshow("Display window", edges)
        cv.waitKey(0)
        cv.destroyAllWindows()
    return edges

    
main()
    