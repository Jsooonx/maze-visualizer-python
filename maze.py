import pygame
import sys
from solver import dfs, bfs, astar

# 0 = Walkable path
# 1 = Wall
maze = [
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

# Start and goal positions (row, col)
start = (0, 0)
end = (6, 6)

algorithm = "astar" # dfs, bfs, astar

# Run selected solver
if algorithm == "dfs":
    visit_order, path = dfs(maze, start, end)
elif algorithm == "bfs":
    visit_order, path = bfs(maze, start, end)
else:
    visit_order, path = astar(maze, start, end)

# Initialized pygame
pygame.init()

# Size of each grid
CELL_SIZE = 60

# Dimensions
ROWS = len(maze)
COLS = len(maze[0])

# Window dimensions
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(f"Maze Visualizer - {algorithm.upper()}")

WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
RED = (220, 50, 50)
PURPLE = (150, 80, 200)
GRAY = (200, 200, 200)
BLUE = (100, 180, 255)
GREEN = (80, 200, 120)

# Clock controls animation speed
clock = pygame.time.Clock()
step_index = 0
show_path = False

# Draw maze grid
def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            
            # Convert grid coordinate to screen coordinate
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            
            # Choose color depending on wall or path
            if maze[row][col] == 1:
                color = BLACK
            else:
                color = WHITE
                
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)

# Draw visited nodes
def draw_visited():
    
    # Only draw nodes explored so far
    for row, col in visit_order[:step_index]:
        rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, BLUE, rect)
        pygame.draw.rect(screen, GRAY, rect, 1)


# Draw final path
def draw_path():
    
    for row, col in path:
        
        rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, GREEN, rect)
        pygame.draw.rect(screen, GRAY, rect, 1)

# Draw start and end nodes
def draw_start_end():
    sr, sc = start
    er, ec = end
    
    # Start node
    pygame.draw.rect(screen, RED, (sc * CELL_SIZE, sr * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    # Goal node
    pygame.draw.rect(screen, PURPLE, (ec * CELL_SIZE, er * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Main program loop
def main():
    global step_index, show_path
    
    while True:
        # Handle window events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Animation logic
        if step_index < len(visit_order):
            step_index += 1
        else:
            show_path = True
        
        # Draw everything
        screen.fill(WHITE)
        draw_grid()
        draw_visited()
        
        if show_path:
            draw_path()
            
        draw_start_end()
        pygame.display.flip()
        # Animation speed
        clock.tick(8)

# Run program
if __name__ == "__main__":
    main()