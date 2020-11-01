import gym
import pygame as pg
import random
from PhysicsObject import PhysicsObject
import numpy as np

class Game(gym.Env):
    
    def __init__(self,screen_width=800, screen_height=600):
        pg.init()
        self.screen_width=screen_width
        self.screen_height=screen_height

        self.screen = pg.display.set_mode((screen_width,screen_height))
        self.running = True
        self.game_over = True
        self.object = PhysicsObject(self,np.array([100,100],dtype=np.float64))
        self.reset()

    def click(event):
        print("click")
        pass
    def keyup(event):
        print("keyup")
        pass
    def events(self):
        for event in pg.event.get():
            if event.type ==pg.QUIT:
                self.running = False
            elif event.type == pg.KEYUP:
                keyup(event)
            elif event.type == pg.MOUSEBUTTONDOWN:
                click(event)

    def reset(self):
        self.game_over = False

    def step(self,action):
        self.object.vel=np.array([1,1],dtype=np.float64)
        self.object.update()
      #  return _,_,self.game_over,{}

    
    def draw(self):
        self.screen.fill((0,0,0))
        pg.draw.circle(self.screen,(255,255,255),self.object.pos,10)
    
    def render(self,mode="human"):
        pass

if __name__ == "__main__":
    game=Game()
    print(game)
    while game.running:
        game.draw()
        game.events()
        game.step(1)
        pg.display.update()

