import gym
import torch
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
import yaml

# Load config
with open("configs/drone_config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Create environment
env = make_vec_env(config["env_name"], n_envs=1)

# Load trained model
model = PPO.load("checkpoints/ppo_drone_policy.zip", env=env)

obs = env.reset()
done = False
total_reward = 0.0

while not done:
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    total_reward += reward[0]

print(f"Test completed. Total reward: {total_reward}")
