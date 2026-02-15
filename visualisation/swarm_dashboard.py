import pygame
import numpy as np

WIDTH = 800
HEIGHT = 800
FPS = 30

DRONE_COLOR = (0, 255, 0)
OBSTACLE_COLOR = (255, 0, 0)
TARGET_COLOR = (0, 0, 255)

DRONE_SIZE = 5
OBSTACLE_SIZE = 8
TARGET_SIZE = 10


class SwarmDashboard:
    def __init__(self, env):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Swarm Real-Time Dashboard")
        self.clock = pygame.time.Clock()
        self.env = env

    def draw_drones(self):
        for drone in self.env.drones:
            x = int(drone.position[0] * WIDTH)
            y = int(drone.position[1] * HEIGHT)
            pygame.draw.circle(self.screen, DRONE_COLOR, (x, y), DRONE_SIZE)

    def draw_obstacles(self):
        if hasattr(self.env, "obstacles"):
            for obs in self.env.obstacles:
                x = int(obs[0] * WIDTH)
                y = int(obs[1] * HEIGHT)
                pygame.draw.circle(self.screen, OBSTACLE_COLOR, (x, y), OBSTACLE_SIZE)

    def draw_targets(self):
        if hasattr(self.env, "targets"):
            for tgt in self.env.targets:
                x = int(tgt[0] * WIDTH)
                y = int(tgt[1] * HEIGHT)
                pygame.draw.circle(self.screen, TARGET_COLOR, (x, y), TARGET_SIZE)

    def render(self):
        self.screen.fill((0, 0, 0))
        self.draw_drones()
        self.draw_obstacles()
        self.draw_targets()
        pygame.display.flip()

    def run(self, policy_fn=None):
        running = True

        state = self.env.reset()

        while running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if policy_fn:
                actions = policy_fn(state)
            else:
                actions = np.random.uniform(-1, 1, (len(self.env.drones), 2))

            state, reward, done, _ = self.env.step(actions)

            self.render()

        pygame.quit()
