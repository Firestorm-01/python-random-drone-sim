import numpy as np

class Drone:
    def __init__(self):
        # Random starting position (0 → 1 normalized)
        self.position = np.random.rand(2)

    def move(self, action):
        """
        action = [dx, dy]
        """
        self.position += action * 0.02
        self.position = np.clip(self.position, 0, 1)
