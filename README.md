# Pathfinding Algorithm Visualizer

A Python project that visualizes and compares pathfinding algorithms on grid-based mazes using Pygame.

## Features
- Visualizes how algorithms explore a maze step-by-step
- Compares three algorithms: DFS, BFS, and A*
- Highlights visited nodes and the final path
- Displays statistics (nodes explored and path length)
- Automatically cycles through all algorithms
- Supports custom mazes via `input.py`
- Includes multiple sample mazes with different difficulty levels

## Algorithms
- **DFS (Depth-First Search)** = explores one path deeply before backtracking
- **BFS (Breadth-First Search)** = explores level by level and guarantees the shortest path in an unweighted grid
- **A\*** = uses a heuristic (Manhattan distance) to guide the search toward the goal

## Project Structure
pathfinding-algorithm-visualizer/
- maze.py = visualization and animation
- solver.py = DFS, BFS, and A* implementations
- input.py = maze configuration (maze, start, end)
- maze_samples.txt = sample mazes for testing

## Requirements
Python
pygame

Install pygame:
```
pip install pygame
```
## Run Instructions
```
python main.py
```
## Maze Format
0 = walkable path  
1 = wall

Example:
```
maze = [
[0,0,1,0],
[0,0,1,0],
[1,0,0,0],
[1,1,1,0]
]

start = (0,0)  
end = (3,3)
```

## Output
<img src="assets/pathfindingdemo.gif" width="700">

## Comparison Insight
This project compares how DFS, BFS, and A* behave on the same maze:
- DFS may find a path quickly, but it does not guarantee the shortest path.
- BFS guarantees the shortest path in an unweighted grid, though it may explore more nodes
- A* improves efficiency by guiding the search with a Manhattan-distance heuristic
Example:
- DFS: Nodes explored = 69, Path length = 49
- BFS: Nodes explored = 58, Path length = 33
- A*: Nodes explored = 40, Path length = 33
