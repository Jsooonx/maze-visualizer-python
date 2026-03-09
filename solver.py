from collections import deque
import heapq

# Get valid neighboring cells
def get_neighbors(position, maze):
    row, col = position
    neighbors = []
    
    # Possible movement directions: up, down, left, right
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]
    
    rows = len(maze)
    cols = len(maze[0])
    
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc
        
        # Check whether the new position is still inside the grid
        if 0 <= new_row < rows and 0 <= new_col < cols:
            
            # Check whether the cell is walkable
            if maze[new_row][new_col] == 0:
                neighbors.append((new_row, new_col))
                
    return neighbors

# Reconstruct final path from end back to start
def reconstuct_path(parent, start, end):
    # Special case
    if start == end:
        return [start]
    
    # If end is not in parent, that means no path was found
    if end not in parent:
        return[]
    
    path = []
    current = end
    
    # Trace backward
    while current != start:
        path.append(current)
        current = parent[current]
        
    # Add start node
    path.append(start)
    
    # Reverse so the path goes from start to end
    path.reverse()
    return path

# DFS
def dfs(maze, start, end):
    stack = [start]
    visited = set([start])
    parent = {}
    visit_order = []
    
    while stack:
        # Take the most recent added node
        current = stack.pop()
        visit_order.append(current)
        
        # Stop if goal is reached
        if current == end:
            path = reconstuct_path(parent, start, end)
            return visit_order, path
        
        # Explore neighbors
        for neighbor in get_neighbors(current, maze):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                stack.append(neighbor)
                
    # No path found
    return visit_order, []

# BFS
def bfs(maze)