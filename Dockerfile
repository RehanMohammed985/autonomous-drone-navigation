# Use official Python base image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire repo
COPY . .

# Install ROS2 dependencies (basic example, adjust if needed)
RUN apt-get update && \
    apt-get install -y curl gnupg2 lsb-release && \
    curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add - && \
    echo "deb http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2.list && \
    apt-get update && apt-get install -y ros-foxy-desktop

# Source ROS2 environment when running container
CMD ["/bin/bash", "-c", "source /opt/ros/foxy/setup.bash && bash"]
