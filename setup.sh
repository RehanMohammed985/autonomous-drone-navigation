#!/bin/bash

echo "Starting environment setup..."

# Update and upgrade system packages (Linux only)
sudo apt-get update && sudo apt-get upgrade -y

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Install ROS2 (for Ubuntu 20.04, adapt if needed)
sudo apt update && sudo apt install -y curl gnupg2 lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update
sudo apt install -y ros-foxy-desktop

# Source ROS2 setup
echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc
source ~/.bashrc

# Install AirSim dependencies (example)
sudo apt-get install -y libpng-dev libjpeg-dev libtiff-dev
pip install msgpack-rpc-python

echo "Setup complete. Please restart your terminal or source ~/.bashrc."
