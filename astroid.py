import gym
import Bullet
env = gym.make("MountainCar-v0")
env.reset()
for i in range(1000):
    env.render()
    env.step(env.action_space.sample())
env.close()