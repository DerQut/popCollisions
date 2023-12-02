import ui_elements
import window
import assets

import pygame
from pygame.locals import *

from tkinter import messagebox


def loop_action():
    ...


def button_handler(down, event_key, needs_shifting, is_shifting):

    if down:
        ...


program_window = window.Window(1280, 720, DOUBLEBUF, assets.bg_colour, "Paint")
