from env.swarm_env import SwarmEnv
from visualisation.swarm_dashboard import SwarmDashboard

env = SwarmEnv()
dashboard = SwarmDashboard(env)

dashboard.run()

