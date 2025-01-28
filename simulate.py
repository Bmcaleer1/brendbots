import time
import pybullet as p

for i in range(1000):
    p.stepSimulation()
    time.sleep(1 / 60)
    print(f"Iteration {i}")
p.disconnect()