import gymnasium as gym
import numpy as np
import time

# --- PD Controller Parameters ---
KP = 20.0
KD = 2.5

# --- Environment Setup ---
env = gym.make("Pendulum-v1", render_mode="human")
fps = env.metadata.get("render_fps", 60)
dt = 1.0 / fps


# Start with minimal random disturbances
def upright_start(env):
    obs, info = env.reset()
    theta = np.random.uniform(-1, 1)
    theta_dot = np.random.uniform(-0.5, 0.5)
    env.unwrapped.state = np.array([theta, theta_dot])
    obs = env.unwrapped._get_obs()
    return obs


obs = upright_start(env)

print("Running PD control with disturbances — press Ctrl+C to stop.")

# --- Simulation ---
try:
    while True:
        # Observing system state
        cos_theta, sin_theta, theta_dot = obs
        theta = np.arctan2(sin_theta, cos_theta)

        # PD Control
        torque = -KP * theta - KD * theta_dot

        # Random disturbances
        disturbance = 0.0
        if np.random.rand() < 0.01:
            disturbance = np.random.uniform(-3, 3)
            print(f"Disturbance torque: {disturbance:.2f}")

        total_torque = np.clip(torque + disturbance, -2.0, 2.0)

        # Environment step
        obs, reward, terminated, truncated, info = env.step([total_torque])
        time.sleep(dt)

        # Reset
        if terminated or truncated:
            print("Environment resetted...")
            obs = upright_start(env)
except KeyboardInterrupt:
    print("\nStopped by user.")
finally:
    env.close()
