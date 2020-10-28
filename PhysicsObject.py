import numpy as np


class PhysicsObject:

    def __init__(self, game, pos):
        self.game = game
        self.pos = pos
        self.vel = np.zeros(2)
        self.acc = np.zeros(2)
        self.speed = 1
        self.friction = 0.9
        self.margin = 0
        
    def update(self):
        self.vel += self.acc
        self.pos += self.vel*self.speed
        self.acc *= 0
        self.vel *= self.friction

        width = self.game.screen_width
        height = self.game.screen_height
        if self.pos[0] > width+self.margin:
            self.pos[0] -= (width+self.margin*2)
        elif self.pos[0] < -self.margin:
            self.pos[0] += (width+self.margin*2)
        if self.pos[1] > height+self.margin:
            self.pos[1] -= (height+self.margin*2)
        elif self.pos[1] < -self.margin:
            self.pos[1] += (height+self.margin*2)