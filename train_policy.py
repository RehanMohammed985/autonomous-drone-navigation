import gym
import torch
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
import yaml
import os

# Load config
with open("configs/drone_config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Create vectorized environment
env = make_vec_env(config["env_name"], n_envs=config["num_envs"])

# Define policy architecture
policy_kwargs = dict(
    net_arch=[dict(pi=[256, 256], vf=[256, 256])]
)

# Initialize PPO model
model = PPO(
    "MlpPolicy",
    env,
    verbose=1,
    learning_rate=config["learning_rate"],
    n_steps=config["n_steps"],
    batch_size=config["batch_size"],
    gamma=config["gamma"],
    policy_kwargs=policy_kwargs,
    tensorboard_log="./ppo_tensorboard/"
)

# Train the model
model.learn(total_timesteps=config["total_timesteps"])

# Save the trained model
os.makedirs("checkpoints", exist_ok=True)
model.save("checkpoints/ppo_drone_policy")
print("Training complete and model saved to checkpoints/ppo_drone_policy.zip")
