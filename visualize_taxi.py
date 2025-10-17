# visualize_taxi.py
# Visualize trained Taxi-v3 agent


import numpy as np
import gymnasium as gym
import time

# Load Q-table
Q = np.load("q_table.npy")
print(" Q-table loaded successfully!")

# Create Taxi-v3 environment with human render mode
env = gym.make("Taxi-v3", render_mode="human")

# Run the trained agent for a few episodes
for ep in range(3):
    state, _ = env.reset()
    done = False
    total_reward = 0
    steps = 0

    while not done:
        # Choose the best learned action
        action = int(np.argmax(Q[state]))
        next_state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
        state = next_state
        total_reward += reward
        steps += 1
        time.sleep(0.25)  # slow down for visibility

    print(f"Episode {ep + 1}: Reward = {total_reward}, Steps = {steps}")

env.close()
print('🎬 Visualization complete.')
