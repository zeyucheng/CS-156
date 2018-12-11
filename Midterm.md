# Midterm
fall 2018 
## Question 1
Consider an agent solving the sliding puzzle.

![sliding.png](https://i.imgur.com/cL24OH7.png)

Which of the following are properties of its environment? **Check ALL that apply.**

**Please note that there is a penalty for marking wrong answers.**

>!  **fully observable**
>!  dynamic
>!  stochastic
>! **sequential**

## Question 2
Consider the state space graph shown below. S is the start state and G is the goal state. The costs for each edge are shown on the graph. Ties are resolved alphabetically. The heuristic values for each state are also included.

1. What **nodes** are expanded when we apply uniform cost graph search?
>! **S, S-A, S-C, S-A-B, S-A-B-G**
2. What **nodes** are expanded when we apply the A* graph search?
>! **S, S-C, S-A, S-A-B, S-A-B-G**

Reminder: B is a state, S-C-B and S-A-B are nodes.

Please list the **nodes in the order they are expanded** and assume that ties are resolved alphabetically.

![astar2.png](https://i.imgur.com/BGDMcD0.png)

## Question 3
Consider the following search problem where S is the start state and G is the goal state.

Is the heuristic h consistent? Please explain.

![cons1.png](https://i.imgur.com/vE4v0My.png)

>! The heuristic is not consistent because node D's heuristic cost is more than the cost to get to node C from node D plus the heuristic cost of C. h(D) <= c(D,a,C) + h( C ) === 5 !<=3+1

## Question 4
Four teams from Cal Poly, Foothill, Mission and SJSU are participating in a hackathon.
The results are not out yet but the following information has been leaked:

**The Cal Poly team is not last.
The Foothill team is not first.
The SJSU team is ahead of the Cal Poly team.**

To represent the problem as a CSP, we'll use the following variables:
**C** for the Cal Poly team, **F** for the Foothill team, **M** for the Mission team and **S** for the SJSU team.

Our goal is to assign a value to each variable that will indicate its rank in the hackathon: 1 (for first), 2, 3, 4. **There are no ties.**

**Please list the domain as a set: for example {1,2,3,4}**

What is the domain of the variable C after the unary constraints are applied?
>! {1,2,3}

What is the domain of the variable F after the unary constraints are applied?
>! {2,3,4}

What is the domain of the variable S after the unary constraints are applied and the consistency of the arc S->C is enforced?
>! {1,2}

What is the domain of the variable C after the unary constraints are applied, the consistency of the arc S->C is enforced and then the consistency of the arc C->S is enforced?
>! {2, 3}

## Question 5
Consider the zero-sum game tree shown below.
![enter image description here](https://i.imgur.com/VgN01vx.png)
Triangles that point up, such as at the top node (root), represent choices for the maximizing player (MAX); triangles that point down represent choices for the minimizing player (MIN).

Outcome values for the maximizing player are listed for each leaf node, represented by the values in rectangles.

Assuming that both players act optimally, what is the best score that Max can achieve?
>! 80

Which of the following actions should the maximizing player (MAX) take: Left, Center or Right?
>! Left

Which of the following branches will be pruned when we apply alpha-beta pruning?

A B C D E F G H I J K L M N O P Q R S T U V

If there is more than one branch, please enter them separated by a comma. If no branch is pruned, please write none. Note that if a major branch is pruned, all its sub-branches are also pruned; there is no need to list the sub-branches separately.

>! J, D, T, F

## Question 6
Consider the non zero-sum game tree with 3 players A, B, and C.The leaf utilities are written as tuples (UA, UB, UC,), with the first component UA denoting the utility of that leaf to A, the second component UB denoting the utility of that leaf to B and the third component UC denoting the utility of that leaf to C. A seeks to maximize UA, B seeks to maximize UB, and C seeks to maximize UC.
![enter image description here](https://i.imgur.com/YRlqmwX.png)
Assuming that all the players act optimally, what is the best utility that player A can achieve?
>! 5
Which of the following action should player A take: Left, Center or Right?
>! Left

## Question 7
Consider the map coloring problem shown below. Our goal is to color the 9 squares (A through I) using two colors only: red and blue. Adjacent squares cannot have the same color. Note that A is adjacent to B and A is not adjacent to C, D or E.

![hill1.png](https://i.imgur.com/EBXgatI.png)

To solve the problem using hill climbing, we start with the initial state S shown below.

![hill0.png](https://i.imgur.com/SnMcY9S.png)

This initial state S can be represented as:

A = red, B = red, C = red, D = red, E = red, F = red, G = blue, H = red, I = blue

We define our objective function f as follows:

8 - number of pairs of adjacent squares colored with the same color.

So for our initial state S, we have f(S) = 8 - 6 = 2

The pairs of adjacent states in conflict for state S are: AB, BC, BD, BE, EF and FH.

Given a state, a successor state is obtained by changing the color of a single square from red to blue or from blue to red.

So the following state is a possible successor state of S:

A =  **blue**, B = red, C = red, D = red, E = red, F = red, G = blue, H = red, I = blue

What state do we end up with when we apply hill climbing to our problem and we start from the initial state S? Please identify the resulting state by listing the color associated with each square:

A = ? , B = ?, C = ?, D = ?, E = ?, F = ?, G = ?, H = ?, I = ?

>! A = Blue , B = Red, C = Blue, D = Blue E = Blue, F = Red, G = Blue, H = Blue, I = Blue

## Question 8
Our task is once again to help our agent find the optimal path to a goal, and today our agent is driving a huge moving truck. The agent must get to the customer's address in heavy traffic.

![delivery.png](https://i.imgur.com/2TrPek0.png)

Note that our agent state is determined by a location and an orientation.

Our start state is in D3, with the orientation shown above (the truck pointing North).

Our goal is to get to our customer, waiting patiently in the house in C1.

The black squares such as B2, D2 and D4 are not accessible to our agent.

Our agent can move forward, make a right turn or make a left turn.

Moving forward from any location has a cost of 1. Making a right turn has an additional cost of 5 and because of traffic, making a left turn has an additional cost of 20.

Note that the truck cannot turn in place (staying in the same grid position).

The combined costs (moving forward and making a turn) are shown below:

![cost1.png](https://i.imgur.com/qC4v5Wc.png)

What is the cost of the solution returned by Breadth First Search?
>! 23

What is the cost of the solution returned by Uniform Cost Search?
>! 22

What is the cost of the solution returned by A* Search assuming we have an admissible heuristic?
>! 22
