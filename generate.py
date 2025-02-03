import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")
#variable initialization
#size
length = 1
width = 2
height = 3
#position
x = 0
y = 1.5
z = 1.5
pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length , width, height])

pyrosim.End()