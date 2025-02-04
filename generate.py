import pyrosim.pyrosim as pyrosim



def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(
        name="Box",
        pos=[-3, 2, 0.5],  # Position at the origin
        size=[1, 1, 1]    # Size of the cube
    )
    pyrosim.End()


def Create_Robot():
    pyrosim.Start_URDF("body.urdf")

    # Main body segment
    pyrosim.Send_Cube(name="Base", pos=[1.5, 0, 1.5], size=[1, 1, 1])

    # Joint connecting the base to the rear limb
    pyrosim.Send_Joint(name="Base_RearJoint", parent="Base", child="RearLeg", type="revolute", position=[1, 0, 1])

    # Rear limb segment
    pyrosim.Send_Cube(name="RearLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])

    # Joint linking the base to the front limb
    pyrosim.Send_Joint(name="Base_FrontJoint", parent="Base", child="FrontLeg", type="revolute", position=[2, 0, 1])

    # Front limb segment
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])

    # Finalize and save the robot structure
    pyrosim.End()


Create_Robot()
Create_World()