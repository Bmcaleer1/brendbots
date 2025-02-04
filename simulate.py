import time
import pybullet as p
import pybullet_data


p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)

planeID = p.loadURDF("plane.urdf")

# Load the world SDF file
worldID = p.loadSDF("world.sdf")

# Load the robot URDF file
robotID = p.loadURDF("body.urdf")

for i in range(1000):
    p.stepSimulation()
    time.sleep(1 / 60)
    print(f"Iteration {i}")

p.disconnect()