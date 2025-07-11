# Autonomous Drone Navigation System

An advanced AI-powered drone navigation framework designed for real-time obstacle avoidance and path planning. The system integrates deep reinforcement learning (DRL), computer vision, and SLAM-based state estimation to enable autonomous flight in complex, dynamic environments. It supports both high-fidelity simulation via AirSim and real-world deployment on resource-constrained drones like NVIDIA Jetson Nano and Raspberry Pi paired with Intel RealSense cameras.

---

## 🧠 System Overview

- **Perception**: Utilizes YOLOv8 for real-time obstacle detection combined with depth estimation from stereo or RGB-D sensors to create an accurate 3D obstacle map.
- **Localization**: Employs visual-inertial SLAM techniques (ORB-SLAM2 or RTAB-Map) for robust pose estimation and environmental mapping.
- **Control**: Implements a DRL policy trained with Proximal Policy Optimization (PPO) using Stable Baselines3, enabling the drone to navigate safely while optimizing flight efficiency.
- **Fallback Planning**: Incorporates a classical A* path planner on a 2.5D occupancy grid to handle scenarios with low DRL confidence, ensuring safety and reliability.
- **Simulation Environment**: Built on Microsoft AirSim with ROS2 integration, allowing training and testing in diverse simulated environments before real-world deployment.
- **Deployment**: Supports real-time operation on embedded hardware platforms (Jetson Nano, Raspberry Pi) with ROS2 and MAVROS for autopilot communication (e.g., PX4).

---

## 🧰 Technology Stack

- **Programming Languages**: Python 3.8+
- **Machine Learning Frameworks**: PyTorch, Stable Baselines3
- **Computer Vision**: OpenCV, YOLOv8
- **SLAM**: ORB-SLAM2, RTAB-Map
- **Simulation**: AirSim (Unreal Engine), ROS2
- **Autopilot**: PX4 with MAVROS for real drone integration
- **Others**: Gym, PyYAML, Matplotlib, NumPy

---

## 📁 Repository Structure

autonomous-drone-navigation/  
├── train_policy.py            # DRL PPO training pipeline  
├── test_policy.py             # Policy evaluation and testing  
├── configs/                   # YAML configs for drone and training params  
│   └── drone_config.yaml  
├── perception/                # Modules for obstacle detection and depth processing  
│   ├── obstacle_detector.py  
│   └── depth_processor.py  
├── control/                   # DRL policy network and fallback planner  
│   ├── policy_network.py  
│   └── planner.py  
├── sim/                       # AirSim environment wrappers and utilities  
│   └── airsim_env.py  
├── utils/                     # Logging, metrics, and helper functions  
│   └── logger.py  
├── launch/                    # ROS2 and AirSim launch configurations  
│   └── airsim.launch  
└── README.md  

---

## 🚀 Quick Start

### Install dependencies

~bash~
pip install -r requirements.txt
Launch AirSim simulation environment
ros2 launch launch/airsim.launch
Train the DRL navigation policy
python train_policy.py --config configs/drone_config.yaml
Test the trained policy
python test_policy.py --model checkpoints/ppo_drone_policy.zip

🔍Training Details

Reinforcement Learning Algorithm: Proximal Policy Optimization (PPO)
Reward Function:
+1 for moving toward the goal
-10 penalty for collisions
-1 penalty per timestep to encourage efficiency
Training Curriculum: Gradual increase in environment complexity from sparse obstacles to dense dynamic scenarios
Simulation Environment: Microsoft AirSim with ROS2 for realistic sensor and flight dynamics
Evaluation Metrics: Success rate, collision rate, average path length, control latency

📊 Performance Summary

Achieves over 87% success rate in complex, cluttered AirSim test environments
Real-time inference with control loop latency under 20ms on NVIDIA Jetson Nano
Robust generalization to unseen maps and dynamic obstacles through curriculum learning and domain randomization


📎 License

MIT License
