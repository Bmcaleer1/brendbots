import pyrosim.pyrosim as pyrosim



def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(
        name="Box",
        pos=[0, 0, 0.5],  # Position at the origin
        size=[1, 1, 1]    # Size of the cube
    )
    pyrosim.End()
def Create_Robot():
    """
    Create a URDF file named 'body.urdf' containing a simple robot.
    """
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(
        name="Torso",
        pos=[0, 0, 1.5],  # Position of the Torso
        size=[1, 1, 1]    # Size of the Torso
    )
    pyrosim.End()


Create_World()
Create_Robot()