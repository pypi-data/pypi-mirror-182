import sys
from termcolor import cprint
import numpy as np
import time as time


class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            # using number of elements that are out of place
            min = float("inf")
            b_ind = 0
            goal = ((1,2,3),(8,0,4),(7,6,5))
            for ind in range(len(self.frontier)):
                pre = 0
                for i in range(3):
                    for j in range(3):
                        if self.frontier[ind].state[i][j] != goal[i][j]:
                            pre += 1
                if pre < min:
                    min = pre
                    b_ind = ind 
                if min == 0:
                    break
            node = self.frontier[b_ind]
            self.frontier = self.frontier[:b_ind] + self.frontier[b_ind+1:]
            return node
        # else:
            # using distance out of place

        #else:
         #   node = self.frontier[0]
          #  self.frontier = self.frontier[1:]
           # return node

class puzzle8:

    def __init__(self, question):
        self.start = question
        self.solution = None
        self.goal = ((1,2,3),(8,0,4),(7,6,5))


    def find_empty(self,state):
        s=1
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    empty = (i,j)
                    s=0
                    break
            if s==0:
                break
        return empty
        

    def neighbors(self, state):
        x_cord,y_cord = self.find_empty(state)
        new_state = np.zeros(9).reshape(3,3)
        for i in range(3):
            for j in range(3):
                new_state[i,j] = np.array(state)[i,j]
        if 3 > x_cord-1 >= 0 and 3 > y_cord >=0:
            state1 = new_state.copy()
            state1[x_cord-1][y_cord],state1[x_cord][y_cord] = state1[x_cord][y_cord],state1[x_cord-1][y_cord]
        else:
            state1 = None
        if 3 > x_cord+1 >= 0 and 3 > y_cord >=0:
            state2 = new_state.copy()
            state2[x_cord+1][y_cord],state2[x_cord][y_cord] = state2[x_cord][y_cord],state2[x_cord+1][y_cord]
        else:
            state2 = None
        if 3 > x_cord >= 0 and 3 > y_cord-1 >=0:
            state3 = new_state.copy()
            state3[x_cord][y_cord-1],state3[x_cord][y_cord] = state3[x_cord][y_cord],state3[x_cord][y_cord-1]
        else:
            state3 = None
        if 3 > x_cord >= 0 and 3 > y_cord+1 >=0:
            state4 = new_state.copy()
            state4[x_cord][y_cord+1],state4[x_cord][y_cord] = state4[x_cord][y_cord],state4[x_cord][y_cord+1]
        else:
            state4 = None
        candidates = [
            ("move down",state1),
            ("move up",state2),
            ("move right",state3),
            ("move left",state4),
        ]

        result = []
        for action, state in candidates:
            if state is not None:
                state = tuple([tuple(i) for i in state])
                result.append((action, state))
        return result



    def move_right(self,state):
        left_size, right_size = state
        if left_size + right_size <= self.right:
            return (0,left_size+right_size)
        else:
            return (left_size - (self.right - right_size) ,self.right)

    def move_left(self,state):
        left_size, right_size = state
        if left_size + right_size <= self.left:
            return (left_size+right_size,0)
        else:
            return (self.left,right_size - (self.left - left_size))


    def solve(self):
        """Finds a solution to maze, if one exists."""

        # Keep track of number of states explored
        self.num_explored = 0

        # Initialize frontier to just the starting position
        start = Node(state=self.start, parent=None, action=None)
        frontier = QueueFrontier()
        frontier.add(start)

        # Initialize an empty explored set
        self.explored = set()
        
        # Keep looping until solution found
        while True:
            
            # If nothing left in frontier, then no path
            if frontier.empty():
                raise Exception("no solution")

            # Choose a node from the frontier
            node = frontier.remove()
            self.num_explored += 1
            
            # If node is the goal, then we have a solution
            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            # Mark node as explored
            self.explored.add(node.state)

            # Add neighbors to frontier
            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)


ques = ((3,4,5),(7,8,1),(0,6,2))
problem = puzzle8(ques)
s=time.time()
problem.solve()
t=time.time()
print(problem.num_explored)
for i in problem.solution[1]:
    print(i)
print(t-s)
