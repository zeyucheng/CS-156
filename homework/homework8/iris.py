# -----------------------------------------------------------------------------
# Name:        iris
# Purpose:     Homework 8
#
# Author:      Rula Khayrallah
#
# Copyright ©  Rula Khayrallah, 2018
# -----------------------------------------------------------------------------
"""
This module preprocesses the Iris CSV dataset
"""
from vectors import Vector


def read_file(filename, n):
    """
    Read the Iris csv file and construct the feature vectors
    The file is assumed to contain 5 columns:
    sepal length, sepal width, petal length, petal width and training label.
    The first 4 columns will be used as features in the feature vector
    constructed.

    :param filename: Name of the csv file containing iris data
    :param n: The maximum number of examples to process.  If the file length is
        less than n, all the examples will be processed
    :return: A tuple containing two lists:
        A list of feature vectors representing the examples
        A list of the corresponding training labels
    """
    data = []
    labels = []
    with open(filename, 'r', encoding='utf-8') as label_file:
        for each_line in label_file:
            example = each_line.strip().split(',')
            num_features = len(example)
            feature_vector = Vector(num_features)
            feature_vector[0] = 1 # bias
            for count in range(num_features - 1):
                feature = float(example[count])
                feature_vector[count + 1] = feature
            label = example[num_features - 1]
            data.append(feature_vector)
            labels.append(label)
            if len(labels) == n:
                break
    return data, labels