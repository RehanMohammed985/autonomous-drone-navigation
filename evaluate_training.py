import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_training_metrics(log_csv="ppo_training_log.csv"):
    if not os.path.exists(log_csv):
        print(f"Log file {log_csv} not found.")
        return

    data = pd.read_csv(log_csv)
    plt.figure(figsize=(12,6))

    if 'reward' in data.columns:
        plt.subplot(1,2,1)
        plt.plot(data['reward'])
        plt.title("Training Reward Over Time")
        plt.xlabel("Episode")
        plt.ylabel("Reward")

    if 'loss' in data.columns:
        plt.subplot(1,2,2)
        plt.plot(data['loss'])
        plt.title("Training Loss Over Time")
        plt.xlabel("Episode")
        plt.ylabel("Loss")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_training_metrics()
