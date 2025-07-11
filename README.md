# Autonomous Drone Navigation System

**AI-Powered Obstacle Avoidance and Path Planning for Small Drones**

---

## Overview

This project implements a  autonomous navigation system for small drones leveraging computer vision and reinforcement learning techniques. It enables drones to safely navigate complex, dynamic environments by combining:

- Real-time obstacle detection via YOLO-based perception
- Depth processing for spatial understanding
- Reinforcement learning (PPO) based policy control
- A* path planning for global navigation
- Simulation environment integration using Microsoft AirSim
- ROS2 interface for real-world deployment compatibility

---

## Features

- Automated training pipeline using Stable Baselines3 PPO
- Custom AirSim gym environment wrapper for realistic simulation
- Modular codebase separating perception, control, and planning
- Unit tests for core components ensuring reliability
- Containerized development and deployment with Docker
- Continuous Integration setup with GitHub Actions
- Configurable hyperparameters via YAML files

---

## Getting Started

### Prerequisites

- Ubuntu 20.04+ (recommended for ROS2 and AirSim compatibility)
- Python 3.8+
- Docker (optional but recommended)
- AirSim and ROS2 installed (see setup instructions)

### Installation

Clone the repo:

~bash~
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Run the setup script to install dependencies:

./setup.sh
Or build and run the Docker container:

docker build -t drone-nav-system .
docker run -it drone-nav-system
Usage

Training
Configure training parameters in configs/drone_config.yaml.
Run training with:

python train_policy.py
Testing
Evaluate trained policies with:

python test_policy.py
Visualize training progress:

python evaluate_training.py
Project Structure

├── control/               # Policy networks and planners
├── perception/            # Obstacle detection and depth processing
├── sim/                   # AirSim environment wrapper
├── utils/                 # Logger and utilities
├── configs/               # YAML config files
├── tests/                 # Unit tests
├── launch/                # ROS2 launch files
├── Dockerfile             # Container setup
├── setup.sh               # Setup script
├── train_policy.py        # Training script
├── test_policy.py         # Testing script
├── evaluate_training.py   # Training visualization
└── README.md
Contributing

Contributions are welcome! Please fork the repo and open a pull request with your improvements.

License

MIT License — see LICENSE file for details.

