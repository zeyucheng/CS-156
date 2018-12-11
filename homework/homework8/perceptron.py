# -----------------------------------------------------------------------------
# Name:     perceptron
# Purpose:  Homework 8
#
# Author:
#
# -----------------------------------------------------------------------------
"""
Multiclass Perceptron implementation

__init__, init_weights and train have been implemented for you.

Your task for homework 8 is to implement predict and update_weights.
"""
from vectors import Vector
from random import randint


class Perceptron(object):
    """
    Represent the Perceptron object
    The Perceptron object learns from the data when the train method is called
    and can use that knowledge to predict a label for any new example.

    Arguments:
    valid_labels (tuple): the unique labels that will be used.
            For digit recognition: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
            For Iris data: ('Iris-versicolor', 'Iris-virginica', 'Iris-setosa')
    iterations (int):  the number of iterations to be used.  This is specified
            by the user when classifier is invoked. Default is 2.

    Attributes:
    weights (dict):  tke keys are the labels and the values are the weight
            vectors corresponding to each label.
    valid_labels (tuple): the unique labels that will be used.
            For digit recognition: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
            For Iris data: ('Iris-versicolor', 'Iris-virginica', 'Iris-setosa')
    iterations (int):  the number of iterations/epochs to be used.
        This is specified by the user when classifier is invoked. Default is 2.
    """
    def __init__(self, labels, iterations):
        self.weights = {}
        self.valid_labels = labels
        self.iterations = iterations

    def init_weights(self, size):
        """
        Initialize the weights corresponding to each label so that they have
        the same features as the data.  The weights for all the features are
        initialized to 0.
        :param size: The size of the first feature vector in the training data
        :return: None
        """
        for each_label in self.valid_labels:
            self.weights[each_label] = Vector(size)


    def train(self, data, labels):
        """
        Train the perceptron with the given labelled data
        :param data: list of the feature vectors representing training examples
        :param labels: list of the training labels corresponding to the data
        :return: None
        """
        self.init_weights(len(data[0]))
        for iteration in range(1, self.iterations+1):
            print('iteration:', iteration)
            count = 0
            for f in data:
                self.update_weights(f, labels[count])
                count += 1

    def update_weights(self, feature_vector, training_label):
        """
        Update the Perceptron weights based on a single training example
        :param feature_vector (Vector): representing a single training example
        :param training_label: training label corresponding to the example
        :return: None
        """
        # Enter your code and remove the statement below
        prediction = self.predict(feature_vector)
        if prediction != training_label:
            right = self.weights[training_label]
            wrong = self.weights[prediction]
            self.weights[training_label] = right-feature_vector
            self.weights[prediction] = wrong+feature_vector
            # print('hallo')


    def predict(self, feature_vector):
        """
        Predict the label of the example represented by the given feature
        vector
        :param feature_vector (Vector):
        :return: label: One of the labels in self.labels
        """
        # Enter your code and remove the statement below
        p = 0
        label = ''
        for weight in self.weights:
            vector = self.weights[weight]
            sums = vector*feature_vector
            if p > sums:
                label = weight
                p = sums
        if label == '':
            label = self.valid_labels[randint(0, len(self.valid_labels)-1)]
        return label

