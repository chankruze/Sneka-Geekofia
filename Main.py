import random
import pygame
import tkinter as tk
from tkinter import messagebox

# Custom classes
from Snake import Snake
from Cube import Cube
from BonusFrog import BonusFrog


def draw_grid(surface):
    # Length & width of each box
    size = window_size // rows
    # Initial x & y
    x = 0
    y = 0

    # Loop to draw grid's columns & rows
    for l in range(rows):
        # Adjust x for each column
        x += size
        # Adjust y for each row
        y += size
        # Draws vertical line (column) from C1(x,0) to C2(x, width)
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, window_size))
        # Draws vertical line (row) from R1(x,0) to R2(x, width)
        pygame.draw.line(surface, (255, 255, 255), (0, y), (window_size, y))


def update_window(surface):
    # draw nwe window
    surface.fill(bg_color)

    # Show score
    pygame.font.init()  # init fonts
    font = pygame.font.Font(None, 40)  # set font size
    text = font.render(str(score), True, (255, 255, 255))
    surface.blit(text, (0, 0))

    # Snake
    snake.draw(surface)

    # Food
    frog.draw(surface)

    if score > 0 and score % 10 == 0:
        giant_frog.should_span(True)
        giant_frog.span(surface)
    else:
        giant_frog.should_span(False)
        giant_frog.hide(surface, bg_color)

    # draw_grid(surface)
    pygame.display.update()


# method to span
def random_frog(item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda cube: cube.position == (x, y), positions))) > 0:
            continue
        else:
            break

    return x, y


def message_box(subject, content):
    # init top level widget
    root = tk.Tk()
    # always on top
    root.attributes("-topmost", True)
    root.wm_withdraw()
    # widget title
    root.wm_title("Game Over")
    root.geometry("1x1+100+100")
    # show the box
    messagebox.showinfo(subject, content)
    root.destroy()

# def timer(clock, max_time):
#     milli = clock.tick()
#     seconds = milli / 1000
#
#     if (seconds)
#
#     return seconds


def main():
    global window_size, rows, snake, frog, giant_frog, score, bg_color
    window_size = 500
    rows = 50
    score = 0
    bonus = 0

    bg_color = (43, 41, 41)
    frog_color = (0, 255, 0)
    giant_frog_color = (0, 200, 255)

    # initialize the snake yard
    window = pygame.display.set_mode((window_size, window_size))
    pygame.display.set_caption('Sneka Geekofia')

    # initialize snake
    snake = Snake((255, 0, 0), (10, 10))
    # initialize first frog
    frog = Cube(random_frog(snake), color=(0, 255, 0))
    # giant frog
    giant_frog = BonusFrog(random_frog(snake))

    # clock
    fps_clock = pygame.time.Clock()
    clock2 = pygame.time.Clock()
    time = 5

    while True:
        # delay the time
        # pygame.time.delay(0)

        # set Frames Per Second
        fps_clock.tick(20)

        # kick snake's ass to start movement
        snake.move()

        # initial score
        score = len(snake.body) - 1 + bonus

        # when snake kisses food
        if snake.body[0].position == frog.position:
            # increase snake's length
            snake.add_cube()
            # place brand new frog
            frog = Cube(random_frog(snake), color=frog_color)
            giant_frog = BonusFrog(random_frog(snake))

        if snake.body[0].position == giant_frog.position and giant_frog.is_spanned():
            # increase snake's length
            # snake.add_cube()
            # place brand new frog
            bonus += 11
            giant_frog = BonusFrog(random_frog(snake))

        # The death condition
        for x in range(len(snake.body)):
            if snake.body[x].position in list(map(lambda cube: cube.position, snake.body[x + 1:])):
                print('Score: ', score)
                message_box('Game Over !', 'Your score: ' + str(score))
                snake.reset((10, 10))
                score = bonus = 0
                break

        # update the snake yard
        update_window(window)
    pass


# start the game
main()
