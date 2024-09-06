import heapq

class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.neighbors = {}

    def __lt__(self, other):
        return self.heuristic < other.heuristic

def greedy_best_first_search(start, goal):
    heap = [(start.heuristic, start)]
    visited = set()
    path = {}
    cost = {start.name: 0}

    while heap:
        _, current = heapq.heappop(heap)

        if current.name == goal.name:
            path_list = []
            node = current.name
            while node in path:
                path_list.append(node)
                node = path[node]
            path_list.append(start.name)
            path_list.reverse()
            return path_list, cost[current.name]

        if current.name in visited:
            continue

        visited.add(current.name)

        for neighbor, edge_cost in current.neighbors.items():
            if neighbor.name not in visited:
                if neighbor.name not in cost or cost[current.name] + edge_cost < cost[neighbor.name]:
                    cost[neighbor.name] = cost[current.name] + edge_cost
                    path[neighbor.name] = current.name
                heapq.heappush(heap, (neighbor.heuristic, neighbor))

    return None, None

# Create nodes
S = Node('S', 7)
A = Node('A', 6)
B = Node('B', 2)
C = Node('C', 6)
D = Node('D', 3)
G = Node('G', 0)

# Define connections
S.neighbors = {A: 6, C: 6, D: 3}
A.neighbors = {B: 2}
B.neighbors = {G: 0}
C.neighbors = {D: 1}
D.neighbors = {B: 1}

# Run the search
result_path, result_cost = greedy_best_first_search(S, G)

# Print results
if result_path:
    print(f"Path: {' -> '.join(result_path)}")
    print(f"Cost: {result_cost}")
else:
    print("No path found")