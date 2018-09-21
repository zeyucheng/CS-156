# -----------------------------------------------------------------------------
# Name:     informed_search
# Purpose:  Homework 3 - Implement astar and some heuristics
#
# Author: Juan Castillo
#
# -----------------------------------------------------------------------------
"""
A* Algorithm and heuristics implementation 

Your task for homework 3 is to implement:
1.  astar
2.  single_heuristic 
3.  better_heuristic
4.  gen_heuristic  
"""
from math import sqrt, floor

import data_structures


def astar(problem, heuristic):
    """
    A* graph search algorithm
    returns a solution for the given search problem
    :param
    problem (a Problem object) representing the quest
            see Problem class definition in spartanquest.py
    heuristic (a function) the heuristic function to be used
    :return: list of actions representing the solution to the quest
                or None if there is no solution
    """
    # Enter your code here and remove the pass statement below
    closed = set()
    fringe = data_structures.PriorityQueue()
    state = problem.start_state()
    root = data_structures.Node(state)
    fringe.push(root, heuristic(state, problem))

    while True:
        if fringe.is_empty():
            return None
        node = fringe.pop()
        if problem.is_goal(node.state):
            return node.solution()
        if node.state not in closed:
            closed.add(node.state)
            for child_state, action, action_cost in problem.successors(node.state):
                # Tie Breaking
                h = heuristic(child_state, problem)
                # goal = problem.medals.copy().pop()
                # start = problem.start_state()[0]
                # dx1 = state[0][0] - goal[0]
                # dy1 = state[0][1] - goal[1]
                # dx2 = start[0] - goal[0]
                # dy2 = start[1] - goal[1]
                # cross = abs(dx1*dy2 - dx2*dy1)

                # h += cross*0.001

                h *= (1.0 + (1/100))
                # if child_state not in closed:
                child_node = data_structures.Node(child_state, node, action, action_cost + node.cumulative_cost)
                f = child_node.cumulative_cost + h
                fringe.push(child_node, f)



def null_heuristic(state, problem):
    """
    Trivial heuristic to be used with A*. 
    Running A* with this null heuristic, gives us uniform cost search
    :param 
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
    :return: 0
    """
    return 0


def single_heuristic(state, problem):
    """
    A simple heuristic for a single medal that finds the manhattan distance
    This heuristic is admissible because the manhattan distance does not account for the cost
    of the increased cost of the East and West direction thus being optimistic
    .
    :param
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest

    :return: 
    """
    # Enter your code here and remove the pass statement below
    if state[1]:
        return min_distance(state[0], state[1])
    return 0


def better_heuristic(state, problem):
    """
    An improved heuristic over the single heuristic that takes into account the cost of each movement.
    It is admissible because the heuristic calculates at most the true cost to the goal.
    :param 
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
    :return:
    """
    # Enter your code here and remove the pass statement below
    if state[1]:
        start = problem.start_state()[0]
        goal = state[1][0]
        position = state[0]
        D = 1
        D2 = 1

        # Check where the state is in relation to the start state
        if position[1] > goal[1]: # Moved East
            D = 1
        if position[1] < goal[1]: # Moved West
            D = 6
        if position[0] > goal[0]: # Moved South
            D2 = 2
        if position[0] < goal[0]: # Moved North
            D2 = 1
        #
        # if position[0] == goal[1] and (position[0] < 0 or position[0] > 14):
        #     return manhattan_distance(position, goal) + 2
        # if position[0] == goal[0] and (position[1] < 0 or position[1] > 37):
        #     return manhattan_distance(position, goal) + 2
        # row = start[0] - position[0]
        # column = start[1] - position[1]
        # # return D * (row + column) + (D2- 2 * D) * min(row, column)
        # if row <= 0 :
        #     D = 2
        # if column <= 0 :
        #     D2 = 6
        # if row > 0:
        #     D = 1
        # if column > 0:
        #     D2 = 1
        # return 2*7 * manhattan_distance(position, goal)
        # return (D2 * abs(position[0] - goal[0])) * (D + abs(position[1] - goal[1]))
        return (D2 * abs(position[0] - goal[0])) + (D * abs(position[1] - goal[1]))
    return 0


def gen_heuristic(state, problem):
    """
    A heuristic for general problems that uses the manhattan distance. This heuristic works on multiple
    medals. This heuristic is admissible because the sum to the goal divided by goals is optimistic
    :param 
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest 
    :return: 
    """
    if state[1]:
        goals = state[1]
        start = problem.start_state()[0]
        heru = []
        sum  = 0
        position = state[0]

        # for goal in goals:
        #     D = 1
        #     D2 = 1
        #     # Check where the state is in relation to the start state
        #     if position[1] > goal[1]:  # Moved East
        #         D = 1
        #     if position[1] < goal[1]:  # Moved West
        #         D = 6
        #     if position[0] > goal[0]:  # Moved South
        #         D2 = 2
        #     if position[0] < goal[0]:  # Moved North
        #         D2 = 1
        #     heru.append((D2 * abs(position[0] - goal[0])) + (D * abs(position[1] - goal[1])))
        for goal in goals:
            D = 1
            D2 = 1
            # Check where the state is in relation to the start state
            if position[1] > goal[1]:  # Moved East
                D = 1
            if position[1] < goal[1]:  # Moved West
                D = 6
            if position[0] > goal[0]:  # Moved South
                D2 = 2
            if position[0] < goal[0]:  # Moved North
                D2 = 1

            # heru.append(((D2 * abs(position[0] - goal[0])) + (D * abs(position[1] - goal[1])), goal))
            # heru.append(max(((D2  * abs(position[0] - goal[0])), (D * abs(position[1] - goal[1]))), goal))
            # sum += min((D2 * abs(position[0] - goal[0])), (D * abs(position[1] - goal[1])))
            sum += (D2 * abs(position[0] - goal[0])) + (D * abs(position[1] - goal[1]))
        # heru.sort()

        return sum / len(goals)
    return 0


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