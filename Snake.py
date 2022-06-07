import os
import pygame
from enum import Enum
import random

class Direction(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4

speed = 10
window_width = 800
window_height = 800

pygame.init()
pygame.display.set_caption("Snake Grygierek")
window = pygame.display.set_mode((window_width, window_height))


refresh_controller = pygame.time.Clock()

snake_position = [250,250]
snake_body = [[250,250],
             [240,250],
             [230,250]]


food_position = [10, 10]


global score
score = 0


def handle_keys(direction):
    new_direction= direction
    for event in [e for e in pygame.event.get() if e.type == pygame.KEYDOWN]:
        if event.type == pygame.K_UP and direction != Direction.DOWN:
            new_direction = Direction.UP
        if event.type == pygame.K_DOWN and direction != Direction.UP:
            new_direction = Direction.DOWN
        if event.type == pygame.K_RIGHT and direction != Direction.LEFT:
            new_direction = Direction.RIGHT
        if event.type == pygame.K_LEFT and direction != Direction.RIGHT:
            new_direction = Direction.LEFT
    return new_direction

def move_snake(direction):
    if direction == Direction.UP:
        snake_position[1]  -= 10

    if direction == Direction.DOWN:
        snake_position[1]  += 10

    if direction == Direction.LEFT:
        snake_position[1]  -= 10

    if direction == Direction.RIGHT:
         snake_position[1] += 10
    snake_body.insert(0, snake_position)
def game_loop():
   while True:
       direction = handle_keys()


def generate_new_food():
    food_position = [random.randrange(1, (window_width // 10))*10,
                     random.randrange(1, (window_width // 10))*10]




def get_food():
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 10
        generate_new_food()
    else:
        snake_body.pop()

def repaint():
    window.fill(pygame.Color(0, 0, 0))
    for body in snake_body:
        pygame.draw.circle(window, pygame.color(0, 255, 0), (body[0], body[1], 10))
    pygame.draw.rect(window, pygame.Color(255,0,0), pygame.Rect(food_position[0], food_position[1], 10, 10))


def game_over():
    pass
def paint_hud():
    pass

def game_loop():
    direction = Direction.RIGHT
    while True:
        direction = handle_keys(direction)
        move_snake(direction)
        get_food()
        repaint()
        game_over()
        paint_hud()
        pygame.display.update()
        refresh_controller.tick(speed)





if __name__ == "__main__":
    game_loop()
    
    
#Quelle: https://www.youtube.com/watch?v=Gc92z58-Qm4&t=2207s
