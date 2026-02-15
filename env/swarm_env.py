import numpy as np
from drone import Drone


class SwarmEnv:

    def __init__(self, num_drones=20):

        self.num_drones = num_drones

        # Will be filled in reset()
        self.drones = []
        self.obstacles = None
        self.targets = None

    def reset(self):

        # Create drones
        self.drones = [Drone() for _ in range(self.num_drones)]

        # ===== THIS IS WHAT YOU ASKED =====
        # Create random obstacles
        self.obstacles = np.random.rand(10, 2)

        # Create random targets
        self.targets = np.random.rand(3, 2)

        return self.get_state()
    def step(self, actions):

        # Move each drone
        for drone, action in zip(self.drones, actions):
            drone.move(action)

        reward = self.compute_reward()
        done = False

        return self.get_state(), reward, done, {}
    def get_state(self):

        drone_positions = np.array([d.position for d in self.drones])

        state = np.concatenate([
            drone_positions.flatten(),
            self.obstacles.flatten(),
            self.targets.flatten()
        ])

        return state
    def compute_reward(self):

        reward = 0

        for drone in self.drones:
            for target in self.targets:
                dist = np.linalg.norm(drone.position - target)
                reward -= dist

        return reward
