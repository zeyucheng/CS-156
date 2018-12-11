# -----------------------------------------------------------------------------
# Name:        classifier
# Purpose:     Homework 8
#
# Author:      Rula Khayrallah
#
# Copyright ©  Rula Khayrallah, 2018
# -----------------------------------------------------------------------------
"""
A multiclass perceptron classifier

This module preprocesses, trains and classifies data from the following
two datasets:
images of handwritten digits (data and labels in the subfolder digits)
Iris flowers dataset (in the subfolder digits)

Examples:
To train the perceptron on the digits dataset with 2 iterations
using 3000 training examples and 1000 examples in
the validation and test sets (all default values):
python classifier.py digits
The validation output is saved in 'digit_validation_output.txt'
The test output is saved in 'digit_test_output.txt'

To train the perceptron the digits dataset with 5 iterations using only 1500
training examples and 500 examples for validation and test:
python classifier.py digits 5 1500 500 500

To train the perceptron with 10 iterations on the Iris dataset using all the
data available:
python classifier.py iris 10
The validation output is saved in 'iris_validation_output.txt'
The test output is saved in 'iris_test_output.txt'
"""
import argparse
import digits
import iris
from perceptron import Perceptron


def compute_accuracy(predictions, labels):
    """
    Compute the accuracy as the percentage of correct prediction over
    the total number of examples processed
    :param predictions: A list of the predicted labels
    :param labels: A list of the training labels
    :return:
    """
    total = len(labels)
    correct = [predictions[i] == labels[i] for i in range(total)].count(True)
    return correct / total * 100

def report(filename, predictions):
    """
    Write the predictions to the specified file
    :param filename (string): name of the output file
    :param predictions: list of predicted labels
    :return: None
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        for p in predictions:
            outfile.write(f'{p}\n')

def digit_classifier(iterations, training, validation, test):
    """
    Train, validate and test a Perceptron classifier on images of
    handwritten digits.
    The validation output is saved in 'digit_validation_output.txt'
    The test output is saved in 'digit_test_output.txt'
    :param iterations:  Number of iterations for the Perceptron
    :param training: Maximum number of training examples to use
    :param validation: Maximum number of validation examples to use
    :param test: Maximum number of test examples to use
    :return:
    """
    print('Training...')
    data = digits.read_images('digits/trainingimages.txt', training)
    labels = digits.read_labels('digits/traininglabels.txt', training)
    all_labels = tuple(sorted(set(labels)))
    p = Perceptron(all_labels, iterations)
    p.train(data, labels)

    print('Validating...')
    v_data = digits.read_images('digits/validationimages.txt', validation)
    v_labels = digits.read_labels('digits/validationlabels.txt', validation)
    predictions = [p.predict(f) for f in v_data]
    report('digit_validation_output.txt', predictions)
    accuracy = compute_accuracy(predictions, v_labels)
    print(f'Validation Accuracy: {accuracy:.2f}%')

    print('Testing...')
    test_data = digits.read_images('digits/testimages.txt', test)
    test_labels = digits.read_labels('digits/testlabels.txt', test)
    predictions = [p.predict(f) for f in test_data]
    report('digit_test_output.txt', predictions)
    accuracy = compute_accuracy(predictions, test_labels)
    print(f'Test Accuracy: {accuracy:.2f}%')


def iris_classifier(iterations, training, validation, test):
    """
    Train, validate and test a Perceptron classifier on the Iris dataset.
    :param iterations:  Number of iterations for the Perceptron
    :param training: Maximum number of training examples to use
    :param validation: Maximum number of validation examples to use
    :param test: Maximum number of test examples to use
    :return:
    """
    print('Training...')
    data, labels = iris.read_file('iris/trainiris.csv', training)
    all_labels = tuple(sorted(set(labels)))
    p = Perceptron(all_labels, iterations)
    p.train(data, labels)

    print('Validating...')
    v_data, v_labels = iris.read_file('iris/validationiris.csv', validation)
    predictions = [p.predict(f) for f in v_data]
    report('iris_validation_output.txt', predictions)
    accuracy = compute_accuracy(predictions, v_labels)
    print(f'Validation Accuracy: {accuracy:.2f}%')

    print('Testing...')
    test_data, test_labels = iris.read_file('iris/testiris.csv', test)
    predictions = [p.predict(f) for f in test_data]
    report('iris_test_output.txt', predictions)
    accuracy = compute_accuracy(predictions, test_labels)
    print(f'Test Accuracy: {accuracy:.2f}%')


def get_arguments():
    """
    Parse and validate the command line arguments
    :return: (tuple containing the various arguments specified
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset',
                        help='Which dataset?',
                        nargs='?',
                        choices=['digits', 'iris'],
                        default='digits')
    parser.add_argument('iterations',
                        help='How many iterations?',
                        nargs = '?',
                        type=int,
                        default=2)
    parser.add_argument('training',
                        help='Training data set size',
                        nargs = '?',
                        type=int,
                        default=3000)
    parser.add_argument('validation',
                        help='Validation data set size',
                        nargs = '?',
                        type=int,
                        default=1000)
    parser.add_argument('test',
                        help='Test data set size',
                        nargs = '?',
                        type=int,
                        default=1000)
    arguments = parser.parse_args()
    dataset = arguments.dataset
    iterations = arguments.iterations
    training = arguments.training
    validation = arguments.validation
    test = arguments.test
    return dataset, iterations, training, validation, test

def main():
    dataset, iterations, training, validation, test = get_arguments()
    if dataset == 'digits':
        digit_classifier(iterations, training, validation, test)
    elif dataset == 'iris':
        iris_classifier(iterations, training, validation, test)

if __name__ == '__main__':
    main()
