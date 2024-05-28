import logging

import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity as ssim
import cv2

logger = logging.getLogger("desktopenv.metrics.metabase")

def compare_metabase_images(image1_path, image2_path):
    # You would call this function with the paths to the two images you want to compare:
    # score = compare_images('path_to_image1', 'path_to_image2')
    # print("Similarity score:", score)

    if not image1_path or not image2_path:
        return 0

    # Open the images and convert to grayscale
    image1 = Image.open(image1_path).convert('L')
    image2 = Image.open(image2_path).convert('L')

    # Resize images to the smaller one's size for comparison
    image1_size = image1.size
    image2_size = image2.size
    
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    if image1_size > image2_size:
        image1 = cv2.resize(image1, (image2.shape[1], int(image1.shape[0] * image2.shape[1] / image1.shape[1])))
    else:
        image2 = cv2.resize(image2, (image1.shape[1], int(image2.shape[0] * image1.shape[1] / image2.shape[1])))
        
    # calculate the Histogram image of the two images
    H1 = cv2.calcHist([image1], [1], None, [256], [0, 256])
    H1 = cv2.normalize(H1, H1, 0, 1, cv2.NORM_MINMAX, -1)  # normalize the histogram

    H2 = cv2.calcHist([image2], [1], None, [256], [0, 256])
    H2 = cv2.normalize(H2, H2, 0, 1, cv2.NORM_MINMAX, -1)

    # compare the two histograms
    similarity = cv2.compareHist(H1, H2, 0)

    if similarity > 0.91: # Account for image differences due to size change
        return 1
    return 0