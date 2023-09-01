import pygame
import random
import ctypes

debug = False

pygame.init()
pygame.font.init()
pygame.mixer.init()

user32 = ctypes.windll.user32

class display:
    fullscreen = False
    x, y = 240 * 4, 160 * 4
    og_x, og_y = x, y


window = pygame.display.set_mode((display.x, display.y))
pygame.display.set_caption('rhythm tengoku game select')

game_running = True
game_state = None

obamna = False

from bg_square import bg_square
from bg import bg
from menu_opt import menu_opt
from obamna import obamna_


class button_logics():

    def on_click1():
        pygame.quit()
        print('Exiting by user, goodbye :)')
        exit()

class transport():
    pygame = pygame
    window = window
    display = display

    aaron_img = pygame.image.load('assets/aaron.png')   # this image used to be an
                                                        # image of my friend, but
                                                        # it was changed to
                                                        # protect his privacy :)     

class menu_state():

    def __init__(self):
        pygame.mixer.music.load('assets/game_select.mp3')
        pygame.mixer.music.play(-1)

        self.bg = bg(transport=transport)

        self.square_list = []
        self.menu_opt_list = []

        #self.menu_opt_list.append(menu_opt('cursor', 60, 60, button_logics.on_click1, transport))
        
        ## incomplete menu option system ^^^ ##

        for _ in range(60):
            square = bg_square(transport=transport)
            self.square_list.append(square)

        if obamna:
            self.obamna = obamna_(transport=transport)

    def render_text(self, str, pos, color, font=pygame.font.Font('assets/default_font.ttf', 20), center=False):
        text = font.render(str, 1, pygame.Color(color))
        if center:
            text_width = text.get_width()
            text_height = text.get_height()

            pos = (display.x / 2 - text_width / 2, display.y / 2 - text_height / 2)
        window.blit(text,pos)

    def update(self):
        window.fill('black')

        self.bg.exist()

        if obamna:
            self.obamna.exist()

        for square in self.square_list:
            square.exist()

        for opt in self.menu_opt_list:
            opt.exist()

        self.render_text(str(int(clock.get_fps())), (0,0), 'black')



clock = pygame.time.Clock()
game_state = menu_state()

while game_running:

    display.x = window.get_width()
    display.y = window.get_height()

    events = pygame.event.get()

    game_state.update()

    for event in events:
        if event.type == pygame.QUIT:  
           game_running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print('Escaping...')
                game_running = False

            if event.key == pygame.K_F11:
                print('Toggle fullscreen')

                if display.fullscreen == False:

                    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
                    pygame.display.set_mode(screensize, pygame.FULLSCREEN)

                if display.fullscreen == True:

                    display.x, display.y = display.og_x, display.og_y
                    pygame.display.set_mode((display.x, display.y),)

                display.fullscreen = not display.fullscreen

    pygame.display.update()
    clock.tick(60)

print('Goodbye! :)')
pygame.quit()