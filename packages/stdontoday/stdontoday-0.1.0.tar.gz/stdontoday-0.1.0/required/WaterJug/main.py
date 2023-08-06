from termcolor import cprint


class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier:
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
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


class Jug:
    def __init__(self, limits):
        self.explored = None
        self.num_explored = None
        self.start = (0, 0)
        self.goal = (limits[2], 0)
        self.left = limits[0]
        self.right = limits[1]
        self.solution = None

    def neighbors(self, state):
        left_size, right_size = state
        candidates = [
            ("fill left", (self.left, right_size)),
            ("fill right", (left_size, self.right)),
            ("left move right", self.move_right((left_size, right_size))),
            ("right move left", self.move_left((left_size, right_size))),
            ("empty left", (0, right_size)),
            ("empty right", (left_size, 0))
        ]

        result = []
        for action, (r, c) in candidates:
            if 0 <= r <= self.left and 0 <= c <= self.right:
                result.append((action, (r, c)))
        return result

    def move_right(self, state):
        left_size, right_size = state
        if left_size + right_size <= self.right:
            return 0, left_size + right_size
        else:
            return left_size - (self.right - right_size), self.right

    def move_left(self, state):
        left_size, right_size = state
        if left_size + right_size <= self.left:
            return left_size + right_size, 0
        else:
            return self.left, right_size - (self.left - left_size)

    def solve(self):
        """Finds a solution to maze, if one exists."""
        # Keep track of number of states explored
        self.num_explored = 0

        # Initialize frontier to just the starting position
        start = Node(state=self.start, parent=None, action=None)
        frontier = StackFrontier()
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


cprint("Enter the capacity of Jug 1:", "red")
jug1 = int(input())
cprint("Enter the capacity of Jug 2:", "red")
jug2 = int(input())
cprint("Enter the amount of water you require:", "red")
req = int(input())
jug = Jug(list((jug1, jug2, req)))
jug.solve()
act, num = jug.solution
i = 0
print(jug.num_explored)
while i < len(act):
    print(act[i], end=" ")
    print(num[i])
    i += 1
# print(jug.solution)
