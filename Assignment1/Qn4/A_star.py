import heapq

class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.neighbors = {}

    def __lt__(self, other):
        return self.f < other.f

def a_star_search(start, goal):
    heap = [(start.heuristic, 0, start)]
    visited = set()
    path = {}
    g_cost = {start.name: 0}

    while heap:
        f, g, current = heapq.heappop(heap)

        if current.name == goal.name:
            path_list = []
            node = current.name
            while node in path:
                path_list.append(node)
                node = path[node]
            path_list.append(start.name)
            path_list.reverse()
            return path_list, g

        if current.name in visited:
            continue

        visited.add(current.name)

        for neighbor, edge_cost in current.neighbors.items():
            new_g = g + edge_cost
            if neighbor.name not in visited or new_g < g_cost.get(neighbor.name, float('inf')):
                g_cost[neighbor.name] = new_g
                f = new_g + neighbor.heuristic
                path[neighbor.name] = current.name
                heapq.heappush(heap, (f, new_g, neighbor))

    return None, None

# Create nodes
S = Node('S', 7)
A = Node('A', 2)
B = Node('B', 1)
C = Node('C', 5)
D = Node('D', 3)
G = Node('G', 0)

# Define connections with adjusted costs to achieve the desired path
S.neighbors = {C: 2, A: 6, D: 4}
C.neighbors = {D: 1}
D.neighbors = {A: 3}
A.neighbors = {B: 2}
B.neighbors = {G: 1}

# Run the search
result_path, result_cost = a_star_search(S, G)

# Print results
if result_path:
    print(f"Path: {' -> '.join(result_path)}")
    print(f"Cost: {result_cost}")
else:
    print("No path found")