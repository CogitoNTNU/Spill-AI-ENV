import gym
import pygame as pg
import random

class Game(gym.Env):
    
    def __init__(self,screen_width=800, screen_height=600):
        pg.init()
        self.screen_width=screen_width
        self.screen_height=screen_height

        self.screen = pg.display.set_mode((screen_width,screen_height))
        self.running = True
        self.game_over = True
        self.reset()

    def events(self):
        for event in pg.event.get():
            if event.type ==pg.QUIT:
                self.running = False

    def reset(self):
        self.game_over = False

    def step(self,action):
        
        return _,_,self.game_over,{}

    
    def draw(self):
        pg.draw.circle(self.screen,(255,255,255),(random.randint(0,self.screen_width),random.randint(0,self.screen_height)),10)
    
    def render(self,mode="human"):
        pass

if __name__ == "__main__":
    game=Game()
    print(game)
    while game.running:
        game.draw()
        game.events()
        pg.display.update()

