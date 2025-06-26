import numpy as np
import random as rand
from tkinter import messagebox
import pygame
import sys
from heapq import heappop, heappush
a = [
['S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', 'X'], ['X', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X', 'X', ' ', 'X', ' ', 'X', 'X', 'X', ' ', ' ', 'X'], ['X', ' ', 'X', 'X', 'X', 'X', ' ', 'X', ' ', 'X', 'X', ' ', 'X', ' ', 'X',' ', ' ', ' ', 'X', ' '], ['X', ' ', 'X', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X', 'X', 'X', 'X'], ['X', ' ', 'X',' ', 'X', 'X',' ','X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', ' ', 'X', ' ', ' ', 'X'], ['X', ' ', 'X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X', ' ', 'X', ' ', ' ', 'X'], ['X',' ', 'X', ' ', 'X', ' ', 'X', 'X', 'X', 'X', 'X', ' ', 'X', ' ', 'X', ' ', 'X','X',' ', 'X'], ['X', ' ', 'X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X', ' ', 'X', ' ', ' ', ' ', ' ', 'X'], ['X', ' ', 'X', ' ', 'X', ' ', 'X', 'X', 'X', ' ', 'X',' ', 'X',' ', 'X', 'X', 'X', 'X',' ', 'X'], ['X', ' ', 'X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X', ' ', 'X', ' ', ' ', ' ', ' ', 'X', ' ', 'X'], ['X',' ', 'X',' ', 'X', 'X', 'X',' ', 'X', 'X', 'X',' ', 'X',' ', 'X', 'X', ' ', 'X', 'X', 'X'], ['X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', 'X'], ['X',' ', 'X',' ', 'X', 'X', 'X', 'X', 'X',' ','X', 'X','X', 'X','X','X', 'X', 'X',' ', 'X'], ['X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X'], ['X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X ' , ' ' , 'X ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , 'X'], ['X', ' ', 'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X'], [' X ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'E']]
b = [
['S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', 'X'], ['X', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X', 'X', ' ', 'X', ' ', 'X', 'X', 'X', ' ', ' ', 'X'], ['X', ' ', 'X', 'X', 'X', 'X', ' ', 'X', ' ', 'X', 'X', ' ', 'X', ' ', 'X', ' ', ' ', ' ', 'X', 'X'], ['X', ' ', 'X', ' ', ' ', 'X' , ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X', 'X' , 'X', 'X'], ['X', ' ', 'X', ' ', 'X', 'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', ' ', 'X', ' ', ' ', 'X'], ['X' , ' ', 'X' , ' ', 'X' , ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X' , ' ', 'X' , ' ', 'X' , ' ', ' ', 'X'], ['X', ' ', 'X', ' ', 'X', ' ', 'X', 'X', 'X', 'X', 'X', ' ', 'X', ' ', 'X', ' ', 'X', 'X', ' ', 'X'], ['X' , ' ', 'X' , ' ', 'X' , ' ', ' ', ' ', ' ', ' ', 'X' , ' ', 'X', ' ', 'X' , ' ', ' ', ' ', ' ', 'X'], ['X', ' ', 'X', ' ', 'X', ' ', 'X', 'X', 'X', ' ', 'X', ' ', 'X', ' ', 'X', 'X', 'X', 'X', ' ', 'X'], ['X' , ' ', 'X' , ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X' , ' ', 'X', ' ', ' ', ' ', ' ', 'X' , ' ', 'X'], ['X', ' ', 'X', ' ', 'X', 'X', 'X', ' ', 'X', 'X', 'X', ' ', 'X', ' ', 'X', 'X', ' ', 'X', 'X', 'X'], ['X' , ' ', 'X' , ' ', ' ', ' ', ' ', ' ', 'X' , ' ', ' ', ' ', 'X' , ' ', ' ', ' ', ' ', ' ', ' ', 'X'], ['X', ' ', 'X', ' ', 'X', 'X', 'X', 'X', 'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X'], ['X ' , ' ' , 'X ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , 'X'], ['X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X'], ['X ' , ' ' , 'X ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , 'X'], ['X', ' ', 'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X'], [' X ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'E']]big_maze1 = [
['S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', 'X'], ['X', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X', 'X', ' ', 'X', ' ', 'X', 'X', 'X', ' ', ' ', 'X'], ['X', ' ', 'X', 'X', 'X', 'X', ' ', 'X', ' ', 'X', 'X', ' ', 'X', ' ', 'X', ' ', ' ', ' ', 'X', 'X'], ['X', ' ', 'X', ' ', ' ', 'X' , ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X', 'X' , 'X', 'X'], ['X', ' ', 'X', ' ', 'X', 'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', ' ', 'X', ' ', ' ', 'X'], ['X' , ' ', 'X' , ' ', 'X' , ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X' , ' ', 'X' , ' ', 'X' , ' ', ' ', 'X'], ['X', ' ', 'X', ' ', 'X', ' ', 'X', 'X', 'X', 'X', 'X', ' ', 'X', ' ', 'X', ' ', 'X', 'X', ' ', 'X'], ['X' , ' ', 'X' , ' ', 'X' , ' ', ' ', ' ', ' ', ' ', 'X' , ' ', 'X', ' ', 'X' , ' ', ' ', ' ', ' ', 'X'],

['X', ' ', 'X', ' ', 'X', ' ', 'X', 'X', 'X', ' ', 'X', ' ', 'X', ' ', 'X', 'X', 'X', 'X', ' ', 'X'], ['X' , ' ', 'X' , ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X' , ' ', 'X', ' ', ' ', ' ', ' ', 'X' , ' ', 'X'], ['X', ' ', 'X', ' ', 'X', 'X', 'X', ' ', 'X', 'X', 'X', ' ', 'X', ' ', 'X', 'X', ' ', 'X', 'X', 'X'], ['X' , ' ', 'X' , ' ', ' ', ' ', ' ', ' ', 'X' , ' ', ' ', ' ', 'X' , ' ', ' ', ' ', ' ', ' ', ' ', 'X'], ['X', ' ', 'X', ' ', 'X', 'X', 'X', 'X', 'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X'], ['X ' , ' ' , 'X ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , 'X'], ['X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X'], ['X ' , ' ' , 'X ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , 'X'], ['X', ' ', 'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], [' X ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'E']]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
li = [a, b,big_maze1]
ran = rand.choice(li)
maze = np.array(ran)
TILE_SIZE = 30
MAZE_WIDTH = len(ran[0])
MAZE_HEIGHT = len(ran)
SCREEN_WIDTH = MAZE_WIDTH * TILE_SIZE
SCREEN_HEIGHT = MAZE_HEIGHT * TILE_SIZE

def heuristic(a, b):
return abs(a[0] - b[0]) + abs(a[1] - b[1])
def a_star(maze, start, end):
open_list = []
heappush(open_list, (0, start))
parent = {start: None}
g_score = {start: 0}
f_score = {start: heuristic(start, end)}
while open_list: _, current = heappop(open_list)
if current == end:
break
neighbors = get_neighbors(maze, current)
for neighbor in neighbors:
tentative_g_score = g_score[current] + 1
if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
parent[neighbor] = current
g_score[neighbor] =tentative_g_score
f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
heappush(open_list, (f_score[neighbor], neighbor))
path = []
step = end
while step:
path.append(step)
step = parent.get(step)
path.reverse()
return path

def get_neighbors(maze, pos):
neighbors = []
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for direction in directions:
new_pos = (pos[0] + direction[0], pos[1] + direction[1])
if 0 <= new_pos[0] < len(maze) and 0 <= new_pos[1] < len(maze[0]) and
maze[new_pos[0]][new_pos[1]] != 'X':
neighbors.append(new_pos)
return neighbors
def find_start_end(maze):
start = end = None
for i in range(len(maze)):
for j in range(len(maze[0])):
if maze[i][j] == 'S':
start = (i, j)
elif maze[i][j] == 'E':
end = (i, j)
return start, end
start, end = find_start_end(maze)
path = a_star(maze, start, end)
pygame.init()
pygame.display.set_caption("A* Maze Pathfinding")
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
FONT = pygame.font.Font(None, 36)
def draw_maze():

SCREEN.fill(WHITE)
for i in range(len(maze)):
for j in range(len(maze[0])):
if maze[i][j] == 'X':
pygame.draw.rect(SCREEN, BLACK, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))
elif maze[i][j] == 'S':
text = FONT.render('S', True, GREEN)
SCREEN.blit(text, (j * TILE_SIZE + 5, i * TILE_SIZE + 5))
elif maze[i][j] == 'E':
text = FONT.render('E', True, RED)
SCREEN.blit(text, (j * TILE_SIZE + 5, i * TILE_SIZE + 5))
way=[]
def draw_path(path, step):
cost = 0
for pos in path[:step]:
if maze[pos[0]][pos[1]] not in ('S', 'E'):
text = FONT.render('*', True, BLUE)
SCREEN.blit(text, (pos[1] * TILE_SIZE + 5, pos[0] * TILE_SIZE + 5))
cost += 1
if maze[pos[0]][pos[1]] == 'E':
pygame.display.flip()
pygame.time.wait(1000)
message = f"The goal state is reached\nThe total path cost is {cost + 1}" messagebox.showinfo(message=message)
messagebox.showwarning(message="->".join(way))
print(message)
pygame.quit()
sys.exit()
if step < len(path):
pos = path[step]
text = FONT.render('X', True, ORANGE)

SCREEN.blit(text, (pos[1] * TILE_SIZE + 5, pos[0] * TILE_SIZE + 5))
if step > 0:
prev_pos = path[step - 1]
direction = get_direction(prev_pos, pos)
if direction:
message = f"Moving {direction}" pygame.display.set_caption(message)
way.append(message)
print(message) # Print direction to console
return cost
def get_direction(prev_pos, current_pos):
if prev_pos[0] < current_pos[0]:
return "down" elif prev_pos[0] > current_pos[0]:
return "up" elif prev_pos[1] < current_pos[1]:
return "right" elif prev_pos[1] > current_pos[1]:
return "left" else:
return None
def main():
step = 0
running = True
while running:
for event in pygame.event.get():
if event.type == pygame.QUIT:
running = False
SCREEN.fill(WHITE)
draw_maze()
cost = draw_path(path, step)

pygame.display.flip()
step += 1
CLOCK.tick(3)
pygame.quit()
if __name__ == "__main__":
main()
