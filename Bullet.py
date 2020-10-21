import math
class Bullet:

    def __init__(self, x, y, direction, life=30, bullet_speed=15):
        self.x = x
        self.y = y
        self.direction = direction
        self.life = life
        self.bullet_speed = bullet_speed
    
    def __repr__(self):
        return "Bullet(x=" + str(self.x) + ", y=" + str(self.y) + ", direction=" \
            + str(self.direction) + ", life=" + str(self.life) + ")"

    def update_bullet(self):
        self.x += bullet_speed * math.cos(self.direction * math.pi/180) 
        self.y += bullet_speed * math.sin(self.direction * math.pi/180)
        
        self.life -= 1

    #todo: Tegn bulletfunksjon 




if __name__ == "__main__":
    b = Bullet(1, 1, 90, 40)
    print(b)
    b2 = eval(str(b))
    print(b2)

