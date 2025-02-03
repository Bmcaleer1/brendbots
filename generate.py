import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")
#variable initialization
#size
length = 1
width = 1
height = 1
#position
x = 0
y = 0.5
z = 0.5
#position 2
x2=1
y2=0.5
z2=1.5
pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length , width, height])
pyrosim.Send_Cube(name="Box2", pos=[x2,y2,z2], size=[length , width, height])

pyrosim.End()