# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH

    start = problem.getStartState()
    openStack = util.Stack()
    closedStack = util.Stack()
    # print(start)
    openStack.push(start)
    parent = {}
    path = []
    path_stack = util.Stack()
    flag = False
    while (openStack.isEmpty() != True):

        s = openStack.pop()

        if problem.isGoalState(s):
            goal = s
            # path.append(pathnode)
            break;

        neighbors = problem.getSuccessors(s)
        closedStack.push(s)

        # if(flag == True):
        #     pathnode = path_stack.pop()
        #     path.append(pathnode)
        # flag = True
        for i in range(len(neighbors)):

            if (neighbors[i][0] not in closedStack.list and neighbors[i][0] not in openStack.list):
                openStack.push(neighbors[i][0])
                parent[neighbors[i][0]] = (s, neighbors[i][1])
                # path_stack.push(neighbors[i][1])

    while (goal != start):
        temp = parent[goal]
        path.append(temp[1])
        goal = temp[0]

    path.reverse()

    return path

    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # start = problem.getStartState()
    # openQueue = util.Queue()
    # closedQueue = util.Queue()
    # # print(start)
    # pathList = []
    # openQueue.push((start, pathList))
    # parent = {}
    # path_stack = util.Stack()
    # flag = False
    # while (openQueue.isEmpty() != True):
    #
    #     s, path = openQueue.pop()
    #
    #     if problem.isGoalState(s):
    #         goal = s
    #         # path.append(pathnode)
    #         return path
    #         break;
    #
    #     neighbors = problem.getSuccessors(s)
    #
    #     closedQueue.push(s)
    #
    #     # if(flag == True):
    #     #     pathnode = path_stack.pop()
    #     #     path.append(pathnode)
    #     # flag = True
    #     for i in range(len(neighbors)):
    #
    #         if (neighbors[i][0] not in closedQueue.list and neighbors[i][0] not in openQueue.list):
    #             openQueue.push((neighbors[i][0], path.append(neighbors[i][1])))
    #             parent[neighbors[i][0]] = (s, neighbors[i][1])

    # while (goal != start):
    #     temp = parent[goal]
    #     path.append(temp[1])
    #     goal = temp[0]
    #
    # path.reverse()

    # start = problem.getStartState()
    # pathList = []
    # states = util.Queue()
    # states.push((start, pathList))
    #
    # visitedState = util.Queue()
    # while not states.isEmpty():
    #     currentState = states.pop()
    #     if problem.isGoalState(currentState[0]):
    #         break
    #         return path
    #     if currentState not in visitedState.list and currentState not in states.list:
    #         state , path = currentState
    #         successors = problem.getSuccessors(state)
    #         for succ in successors:
    #             newState = succ[0]
    #             if newState not in visitedState.list:
    #                 directions = succ[1]
    #                 pathList = path + [directions]
    #                 states.push((newState, pathList))
    #     visitedState.push((state , pathList))
    #
    # print(path)
    # return path

    # return path

    start = problem.getStartState()
    openQueue = util.Queue()
    closedQueue = util.Queue()
    pathList=[]
    openQueue.push((start,[]))

    while not openQueue.isEmpty():

        s , path = openQueue.pop()

        if problem.isGoalState(s):
            break
            return path

        closedQueue.push(s)

        successors = problem.getSuccessors(s)

        for succ in successors:
            state = succ[0]
            directions = succ[1]

            if state not in openQueue.list and state not in closedQueue.list:
                pathList = path + [directions]
                openQueue.push((state,pathList))
    print(closedQueue.list)
    print(path)
    return path
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    start = problem.getStartState()
    pathList = []
    states = util.PriorityQueue()
    states.push((start, pathList), 0)

    visitedState = []

    while not states.isEmpty():
        state, path = states.pop()
        if problem.isGoalState(state):
            return path
        if state not in visitedState:
            successors = problem.getSuccessors(state)
            for succ in successors:
                newState = succ[0]
                if newState not in visitedState:
                    directions = succ[1]
                    newCost, pathList = path + [directions], path + [directions]
                    states.push((newState, pathList), problem.getCostOfActions(newCost))
        visitedState.append(state)
    return path

    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    pathList = []
    states = util.PriorityQueue()
    states.push((start, pathList), 0)

    visitedState = []

    while not states.isEmpty():
        state, path = states.pop()
        if problem.isGoalState(state):
            return path
        if state not in visitedState:
            successors = problem.getSuccessors(state)
            for succ in successors:
                newState = succ[0]
                if newState not in visitedState:
                    directions = succ[1]
                    newCost, pathList = path + [directions], path + [directions]
                    newCost = problem.getCostOfActions(newCost) + heuristic(newState, problem)
                    states.push((newState, pathList), newCost)
        visitedState.append(state)
    return path

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
