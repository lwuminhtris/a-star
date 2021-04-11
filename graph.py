import heapq
import random
import functools

class PriorityQueue:
    def __init__(self):
        self.elements = {}

    def empty(self) -> bool:
        return len(self.elements) == 0
    
    def put(self, item, priority) -> None:
        self.elements[item] = priority
    
    def get(self) -> int:
        best_item, best_priority = None, None
        for item, priority in self.elements.items():
            if best_priority is None or priority < best_priority:
                best_item, best_priority = item, priority
        
        del self.elements[best_item]
        return best_item

class WeightedGraph: 
    def __init__(self, width: int, height: int, ifRandom = False):
        self.width = width
        self.height = height
        self.grid = []
        self.matrix = ()

        for i in range(0, self.width):
            self.grid.append([1 for j in range(0, self.height)])

        if ifRandom == True:
            for i in range(0, self.width):
                for j in range(0, self.height):
                    self.grid[i][j] = random.randint(0, 99)

    # start state initialzation
    def start_location(self) -> list:
        return [random.randint(0, self.width - 1), random.randint(0, self.height - 1)]

    # end state initialization
    def end_location(self) -> list:
        return [random.randint(0, self.width - 1), random.randint(0, self.height - 1)]

    # return the cost from box A -> box B nearby
    def cost(self, from_box: tuple, to_box: tuple) -> int:
        return self.grid[to_box[0]][to_box[1]]

    # estimates the distance between the current box and the end
    def heuristic(self, current: list, end: list):
        return abs(current[0] - end[0]) + abs(current[1] - end[1])

    def show_grid(self):

        print("Matrix: ")
        for i in range(0, self.width):
            for j in range(0, self.height):
                if self.grid[i][j] not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    print(" {} ".format(self.grid[i][j]), end="")
                else:
                    print(" 0{} ".format(self.grid[i][j]), end="")
            print("")

    # insert the weight of a box
    def insert_box_weight(self, location: list, weight: int) -> None:
        self.grid[location[0]][location[1]] = weight

    # return the neighbors of a node
    def get_neighbors(self, location: list) -> list: 
        neighbors = []
        if location[0] + 1 < self.width:
            neighbors.append((location[0] + 1, location[1]))

        if location[1] + 1 < self.height: 
            neighbors.append((location[0], location[1] + 1))

        if location[0] - 1 >= 0:
            neighbors.append((location[0] - 1, location[1]))

        if location[1] - 1 >= 0: 
            neighbors.append((location[0], location[1] - 1))
        
        return neighbors  

    # find the shortest possible path betwwen the start and end
    def a_star(self, start: list, end: list) -> None: 
        frontier = PriorityQueue()
        # we have to convert list -> tuple as dictionary key requires unmutable data type
        frontier.put((start[0], start[1]), 0)
        came_from = {} # came_from[location] = int
        cost_so_far = {} # cost_so_far[location] = int
        came_from[(start[0], start[1])] = 0
        cost_so_far[(start[0], start[1])] = 0
        
        while not frontier.empty():
            current = frontier.get()

            if current == end:
                break

            for next in self.get_neighbors(current):
                new_cost = cost_so_far[(current[0], current[1])] + self.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[(next[0], next[1])]:
                    cost_so_far[(next[0], next[1])] = new_cost
                    priority = new_cost + self.heuristic(next, end)
                    frontier.put((next[0], next[1]), priority)
                    came_from[(next[0], next[1])] = current
        return came_from, cost_so_far

    # draw the line on the grid
    def draw_the_line(self, start: list, end: list):
        (came_from, cost_so_far) = self.a_star(start, end)
        location = came_from[tuple(end)]

        line = []

        while tuple(start) != location:
            #print(location)
            line.append(location)
            location = came_from[tuple(location)]

        self.grid[start[0]][start[1]] = "st"
        self.grid[end[0]][end[1]] = "fi"
        for x in line:
            self.grid[x[0]][x[1]] = " *" 

        self.show_grid()

'''
x = WeightedGraph(12, 10, True)
# x.insert_box_weight([1, 1], 1)
x.insert_box_weight([1, 0], 2)
x.insert_box_weight([0, 2], 2)
x.insert_box_weight([2, 0], 4)
# x.insert_box_weight([2, 1], 7)
x.show_grid()


(came_from, cost_so_far) = x.a_star([0, 0], [3, 3])
for j in came_from:
    print(j, " is from ", came_from[j])

x.draw_the_line([0, 0], [3, 3])
'''

