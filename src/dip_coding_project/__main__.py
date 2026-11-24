from dip_coding_project.detection import canny_edge_detection
from dip_coding_project.image_io import load_image
from dip_coding_project.preprocessing import grayscale_image

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

    img = load_image("/Users/bennet/Desktop/Istanbul Uni/Digital Image Processing/dip_coding_project/sample/34469040.jpg", False)
    gray_img = grayscale_image(img, False)
    edges = canny_edge_detection(gray_img, True)


if __name__ == "__main__":
    main()
