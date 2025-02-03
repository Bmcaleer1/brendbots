import pyrosim.pyrosim as pyrosim



def Create_World():
    """
    Create an SDF file named 'world.sdf' containing a single cube.
    """
    pyrosim.Start_SDF("world.sdf")

    pyrosim.Send_Cube(
        name="Box",
        pos=[-4, 4, 0.5],
        size=[1, 1, 1]
    )

    pyrosim.End()