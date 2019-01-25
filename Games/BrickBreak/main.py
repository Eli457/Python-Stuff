#Brick Break Game
import pygame as pg
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        #initailize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        #start a new game
        self.all_sprites = pg.sprite.Group()
##        self.walls = pg.sprite.Group()
##        self.player = Player(self)
##        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        #Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        #Game Loop - Update
        self.all_sprites.update()

    def events(self):
        #Game Loop - events
        for event in pg.event.get():
            #checks for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        #Game Loop - draw
        self.screen.fill(ORANGE)
##        self.all_sprites.draw(self.screen)
##        self.draw_text(str(self.score), 22, WHITE, WIDTH / 2, 15)
##        #*after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
