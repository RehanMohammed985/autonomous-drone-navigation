import gym
from gym import spaces
import numpy as np
import airsim

class AirSimDroneEnv(gym.Env):
    def __init__(self):
        super(AirSimDroneEnv, self).__init__()
        self.client = airsim.MultirotorClient()
        self.client.confirmConnection()
        self.client.enableApiControl(True)
        self.client.armDisarm(True)

        # Define action and observation space
        # Actions: [pitch, roll, throttle, yaw_rate]
        self.action_space = spaces.Box(low=np.array([-1,-1,0,-1]), high=np.array([1,1,1,1]), dtype=np.float32)
        
        # Observation: Example: position (x,y,z), velocity (x,y,z), orientation quaternion (x,y,z,w)
        obs_low = np.array([-1000]*3 + [-100]*3 + [-1]*4)
        obs_high = np.array([1000]*3 + [100]*3 + [1]*4)
        self.observation_space = spaces.Box(low=obs_low, high=obs_high, dtype=np.float32)

    def reset(self):
        self.client.reset()
        self.client.enableApiControl(True)
        self.client.armDisarm(True)
        self.client.takeoffAsync().join()
        obs = self._get_obs()
        return obs

    def step(self, action):
        pitch, roll, throttle, yaw_rate = action
        # Command drone based on action inputs
        self.client.moveByAngleThrottleAsync(pitch, roll, throttle, yaw_rate, duration=0.05).join()

        obs = self._get_obs()
        reward = self._compute_reward(obs, action)
        done = self._check_done(obs)
        info = {}
        return obs, reward, done, info

    def _get_obs(self):
        state = self.client.getMultirotorState()
        pos = state.kinematics_estimated.position
        vel = state.kinematics_estimated.linear_velocity
        ori = state.kinematics_estimated.orientation
        obs = np.array([pos.x_val, pos.y_val, pos.z_val,
                        vel.x_val, vel.y_val, vel.z_val,
                        ori.x_val, ori.y_val, ori.z_val, ori.w_val], dtype=np.float32)
        return obs

    def _compute_reward(self, obs, action):
        # Placeholder reward function
        # Penalize collision or large deviations
        collision_info = self.client.simGetCollisionInfo()
        if collision_info.has_collided:
            return -10.0
        # Reward for moving forward or staying stable can be added here
        return 0.1

    def _check_done(self, obs):
        collision_info = self.client.simGetCollisionInfo()
        if collision_info.has_collided:
            return True
        # Additional done conditions can be added (e.g., time limit, out of bounds)
        return False
