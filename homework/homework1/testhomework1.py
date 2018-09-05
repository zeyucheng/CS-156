# -----------------------------------------------------------------------------
# Name:         testhomework1
# Purpose:      Test functions for homework 1
#
# Author:       Rula Khayrallah
# -----------------------------------------------------------------------------
import homework1
import unittest

class TestHomework1(unittest.TestCase):
    """
    Test case for the 4 functions
    """

    def test_manhattan_distance(self):
        """ test the manhattan_distance function"""
        self.assertEqual(homework1.manhattan_distance((2, 7), (1, 3)), 5)
        self.assertEqual(homework1.manhattan_distance((0, 1), (1, 3)), 3)
        self.assertEqual(homework1.manhattan_distance((2, 7), (4, 2)), 7)
        self.assertEqual(homework1.manhattan_distance((5, 2), (4, 4)), 3)
        self.assertEqual(homework1.manhattan_distance((1, 5), (1, 5)), 0)

    def test_min_distance(self):
        """ test the min_distance function"""
        self.assertEqual(homework1.min_distance((3, 4),
                                                {(1, 2), (4, 5),
                                                 (4, 3), (9, 2), (0, 1)}),
                         2)
        self.assertEqual(homework1.min_distance((3, 4), {(1, 2), (0, 0)}),
                         4)
        self.assertEqual(homework1.min_distance((3, 4), {(3, 4)}),
                         0)
        self.assertIsNone(homework1.min_distance((3, 4), {}))

    def test_farthest_point(self):
        """ test the farthest_point function"""
        self.assertEqual(homework1.farthest_point((3, 4),
                                                  {(1, 2),(4, 5),
                                                   (9, 2),(0, 1)}),
                         (9, 2))

        self.assertEqual(homework1.farthest_point((3, 4),
                                                  {(1, 2), (3, 3), (4, 3)}),
                         (1, 2))
        self.assertIsNone(homework1.farthest_point((3, 4), {}))

    def test_farthest_distance(self):
        """ test the farthest_distance function"""
        self.assertEqual(homework1.farthest_distance([(1, 2), (4, 3), (9, 2),
                                                      (4, 5), (0, 1)]),
                         10)

        self.assertEqual(homework1.farthest_distance([]), 0)


if __name__ == '__main__':
    unittest.main()
