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

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
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
    return  [s, s, w, s, w, w, s, w]


class node:
  def __init__(self,state,direction,parent,cost):
    self.state=state
    self.direction=direction
    self.parent=parent
    self.cost=cost
    self.corners=[False,False,False,False]



def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    frontier = util.Stack()
    Node1 = node(problem.getStartState(), None, None, None)
    frontier.push(Node1)
    expanded = []
    path2 = []
    final = []

    while not frontier.isEmpty():
        state = frontier.pop()
        if problem.isGoalState(state.state):
            x = state
            while (x.parent is not None):
                path2.append(x.direction)
                x = x.parent
            for i in reversed(path2):
                final.append(i)
            return final
        if not state.state in expanded:
            expanded.append(state.state)
            possibility = problem.expand(state.state)
            for child in possibility:
                Nodee = node(child[0], child[1], state, child[2])
                frontier.push(Nodee)



    util.raiseNotDefined()





def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    frontier = util.Queue()
    Node1 = node(problem.getStartState(), None, None,None)
    frontier.push(Node1)
    expanded = []
    path2 = []
    final = []

    while not frontier.isEmpty():
        state = frontier.pop()
        if problem.isGoalState(state.state):
            x = state
            while (x.parent is not None):
                path2.append(x.direction)
                x = x.parent
            for i in reversed(path2):
                final.append(i)
            return final
        if not state.state in expanded:
            expanded.append(state.state)
            possibility = problem.expand(state.state)
            for child in possibility:
                Nodee = node(child[0], child[1], state,child[2])
                frontier.push(Nodee)

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
    frontier = util.PriorityQueue()
    Node1 = node(problem.getStartState(), None, None, heuristic(problem.getStartState(), problem))
    frontier.push(Node1, heuristic(Node1.state, problem))
    expanded = []
    path2 = []
    final = []
    costN = 0
    p=0
    while not frontier.isEmpty():
        state = frontier.pop()
        if problem.isGoalState(state.state):
            x = state
            while (x.parent is not None):
                path2.append(x.direction)
                x = x.parent
            for i in reversed(path2):
                final.append(i)
            return final
        if not state.state in expanded:
            expanded.append(state.state)
            possibility = problem.expand(state.state)
            for child in possibility:
                Nodee = node(None, None, None, 0)
                Nodee.state = child[0]
                Nodee.parent = state
                Nodee.direction = child[1]
                Nodee.cost = child[2] + Nodee.parent.cost
                costN = Nodee.cost + heuristic(Nodee.state, problem)
                frontier.push(Nodee, costN)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
