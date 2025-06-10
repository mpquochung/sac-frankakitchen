import gymnasium as gym
import gymnasium_robotics
from gym_robotics_custom import RoboGymObservationWrapper

gym.register_envs(gymnasium_robotics)

max_episode_steps = 500
env_name = "FrankaKitchen-v1"
task = 'microwave'

env = gym.make(env_name, max_episode_steps=max_episode_steps, tasks_to_complete=[task])
env = RoboGymObservationWrapper(env, goal=task)

observation, info = env.reset()

print(f"Observation shape: {observation}")