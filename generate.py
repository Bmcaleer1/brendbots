import pyrosim.pyrosim as pyrosim


def Create_World():
    pyrosim.Start_SDF("world.sdf")  # start new SDF file

    # Cube initial Position
    x = 2
    y = 2
    z = 0.5

    # Setting initial block size
    length = 1
    width = 1
    height = 1

    pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])

    pyrosim.End()


def Create_Robot():
    # Robot initial Position
    x = 0.5
    y = 0
    z = 0.5

    # Setting initial Torso size
    length = 1
    width = 1
    height = 1

    pyrosim.Start_URDF("body.urdf")

    # torso - root link
    pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])

    # torso_backleg - joint
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])

    # back leg - link
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])

    # torso_frontleg - joint
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])

    # front leg - link
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])
    pyrosim.End()


Create_World()
Create_Robot()