import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy as np
import os

physicsClient = p.connect(p.GUI)    #Connecting to physics engine
p.setAdditionalSearchPath(pybullet_data.getDataPath())  #To load URDF files i think

planeId = p.loadURDF("plane.urdf")  #create floor
robotId = p.loadURDF("body.urdf")
p.setGravity(0,0,-9.8)  #set gravity to -9.8

p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)



for i in range(0,1000):
  p.stepSimulation()
  backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg") #Checks for touch on BackLeg
  frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
  print(f"Step {i}: BackLeg = {backLegSensorValues[i]}, FrontLeg = {frontLegSensorValues[i]}")

  time.sleep(1/60)

np.save('data/backleg_values.npy', backLegSensorValues)
np.save('data/frontleg_values.npy', frontLegSensorValues)
p.disconnect()
print(backLegSensorValues)