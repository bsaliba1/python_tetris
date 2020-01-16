import pygame
import random

# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init()

# GLOBALS VARS
s_width = 700
s_height = 800

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0,)
green = (0, 255, 0)
blue = (0, 0, 255)

grey = (0, 0, 0)

play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

# SHAPE FORMATS

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]


# index 0 - 6 represent shape

class MenuButton:
    def __init__(self, x, y, w, h, label):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.label = label
        self.text_size = 60
        self.button = pygame.Surface((w, h))
        self.button.fill(black)
        draw_text_middle(label, self.text_size, white, self.button)

    def blit_button(self, surface):
        surface.blit(self.button, (self.x, self.y))

    def hover_check(self, surface, mouse_position):
        if self.x < mouse_position[0] < self.x + self.w and self.y < mouse_position[1] < self.y + self.h:
            self.button.fill(grey)
        else:
            self.button.fill(grey)

        self.blit_button(surface)


class Menu:
    def __init__(self, labels=None):

        if labels is None:
            labels = ['Play', 'Leaderboard', 'Credits', 'Extra']

        # Vars
        self.buttons = {}  # dictionary to access all menu button objects
        self.m_width, self.m_height = self.dimensions = (s_width, s_height)
        self.menu = pygame.Surface(self.dimensions)
        self.button_gap = 50  # gap between each button
        self.num_buttons = len(labels)

        self.menu.fill(blue)  # Erase Line later
        position = self.button_gap
        label_i = 0
        button_h = (self.m_height - (self.num_buttons + 1) * self.button_gap) / self.num_buttons
        for i in range(self.num_buttons):
            self.buttons[labels[label_i]] = MenuButton(50, position, self.m_width - 100, button_h, labels[label_i])
            self.buttons[labels[label_i]].blit_button(self.menu)
            position += button_h + 50
            label_i += 1

    def blit_menu(self, surface, position):
        surface.blit(self.menu, position)

    def hover_check(self, surface, mouse_position):
        for _, button in self.buttons.items():
            self.menu.fill(blue)
            button.hover_check(self.menu, mouse_position)
            self.blit_menu(surface, (0, 0))


class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0


def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (0, 0))


def draw_grid(surface, row, col):
    surface.fill((0, 0, 0))
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris', 1, (255, 255, 255))

    surface.blit(label, top_left_x + play_width / 2 - (label.get_width() / 2, 30))


def main_menu():
    win = pygame.display.set_mode((s_width, s_height))
    pygame.display.set_caption('Tetris')
    win.fill(white)

    menu = Menu()
    menu.blit_menu(win, (0, 0))
    clock = pygame.time.Clock()

    pygame.display.flip()

    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        mouse_pos = pygame.mouse.get_pos()
        menu.hover_check(win, mouse_pos)
        pygame.display.update()
        clock.tick(15)

    pygame.quit()


main_menu()  # start game
