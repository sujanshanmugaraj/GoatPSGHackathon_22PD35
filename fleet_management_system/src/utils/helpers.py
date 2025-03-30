import heapq
import math

def heuristic(a, b):
    """
    Calculate the Euclidean distance between two points (a and b).
    """
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def reconstruct_path(came_from, start, goal):
    """
    Reconstruct the path from start to goal using the came_from dictionary.
    """
    current = goal
    path = []

    while current != start:
        if current not in came_from:
            print(f"⚠️ Error: Incomplete path. Cannot reach {goal} from {start}.")
            return []
        path.append(current)
        current = came_from[current]

    path.append(start)
    path.reverse()
    return path

def a_star(graph, coordinates, start, goal):
    """
    A* Pathfinding Algorithm to find the shortest path from start to goal.
    """
    # Validate if start and goal nodes exist in the graph and coordinates
    if start not in graph or goal not in graph:
        print(f"❗ Error: Invalid nodes. Start: {start}, Goal: {goal}")
        return []

    if start not in coordinates or goal not in coordinates:
        print(f"❗ Error: Missing coordinates for Start: {start}, Goal: {goal}")
        return []

    open_list = [(0, start)]  # Priority queue: (priority, node)
    came_from = {}
    cost_so_far = {start: 0}

    while open_list:
        current_priority, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, start, goal)

        for neighbor, edge_data in graph[current].items():
            # Ensure valid neighbor data
            if neighbor not in coordinates:
                print(f"⚠️ Warning: Missing coordinates for node {neighbor}. Skipping.")
                continue

            weight = edge_data.get('weight', 1)  # Default to weight=1 if missing
            new_cost = cost_so_far[current] + weight

            # Update path if a better one is found
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(coordinates[neighbor], coordinates[goal])
                heapq.heappush(open_list, (priority, neighbor))
                came_from[neighbor] = current

    print(f"⚠️ No path found between {start} and {goal}")
    return []
