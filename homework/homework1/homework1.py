# -----------------------------------------------------------------------------
# Name:        homework1
# Purpose:     Practice writing Python functions
#
# Author:      Juan Castillo
# -----------------------------------------------------------------------------
"""
Implement some helper functions that will be useful in subsequent assignments
"""


def manhattan_distance(point1, point2):
    """
    Compute the Manhattan distance between two points.
    :param point1 (tuple) representing the coordinates of a point in a plane
    :param point2 (tuple) representing the coordinates of a point in a plane
    :return: (integer)  The Manhattan distance between the two points
    """
    # Enter your code here and remove the pass statement below
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def min_distance(point1, other_points):
    """
    Find the minimum Manhattan distance from point1 to the other points
    :param point1 (tuple) representing the coordinates of a point in a plane
    :param other_points (set of tuples) representing several points in a plane
    :return: (integer) maximum Manhattan distance from point1 to the other
    points

    """
    if other_points:
        return min([manhattan_distance(point1, point) for point in other_points])
    return None


def farthest_point(point1, other_points):
    """
    Find the coordinates of the farthest point to point1
    :param point1 (tuple) representing the coordinates of a point in a plane
    :param other_points(set of tuples) representing several points in a
    plane
    :return: (tuple) the coordinates of the farthest point to point1

    """
    if other_points:
        "I coded this buy don't really understand it"
        return max(other_points, key=lambda point: manhattan_distance(point1, point))
    return None


def farthest_distance(points):
    """
    Find the maximum Manhattan distance between all the points given
    :param points(list of tuples) representing several points in a
    plane
    :return: (integer) maximum Manhattan distance between any two points
    in the list given.
    """
    if points:
        distances = []
        index = 1
        for point in points:
            distances += ([manhattan_distance(point, point2) for point2 in points[index:]])
            index = index + 1
        return max(distances)
    return 0
