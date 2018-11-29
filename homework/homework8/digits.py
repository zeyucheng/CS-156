# -----------------------------------------------------------------------------
# Name:        digits
# Purpose:     Homework 8
#
# Author:      Rula Khayrallah
#
# Copyright ©  Rula Khayrallah, 2018
# -----------------------------------------------------------------------------
"""
This module preprocesses the digit image and label files
"""
IMAGE_SIZE = 28
NUM_FEATURES = IMAGE_SIZE ** 2 + 1
from vectors import Vector

def convert(char):
    """
    Convert a single character in an image to a pixel value: 0 (OFF) or 1 (ON)
    :param char (string)
    :return: 0 or 1
    """
    if char == ' ':
        return 0  # A 0 represents an OFF pixel the image
    else:
        return 1 # A 1 represents an ON pixel the image

def read_images(filename, n):

    """
    Read the digits image file and construct the feature vectors.
    The image is assumed to be 28 x 28 pixels.
    Each pixel represents a feature.

    :param filename: Name of the text file containing the images
    :param n: The maximum number of examples to process.  If the file
            length is less than n, all the examples will be processed
    :return: A list of feature vectors representing the images
    """
    image_row = 0
    image_data = []
    with open(filename, 'r', encoding='utf-8') as image_file:
        for each_line in image_file:
            if image_row == 0:
                if len(image_data) == n:
                    return image_data
                feature_vector = Vector(NUM_FEATURES)
                feature_vector[0] = 1 # bias
                image_data.append(feature_vector)
                feature = 1
            for each_char in each_line[0:IMAGE_SIZE]:
                feature_vector[feature] = convert(each_char)
                feature += 1
            image_row = (image_row + 1) % IMAGE_SIZE
    return image_data

def read_labels(filename, n):
    """
    Read the digits label file and return a list of the training labels.

    :param filename: Name of the text file containing the labels
    :param n: The maximum number of examples to process.  If the file
            length is less than n, all the examples will be processed
    :return: A list of the training labels (list of integers)

    """
    label_data = []
    with open(filename, 'r', encoding='utf-8') as label_file:
        for each_line in label_file:
            label_data.append(int(each_line.strip()))
            if len(label_data) == n:
                break
    return label_data