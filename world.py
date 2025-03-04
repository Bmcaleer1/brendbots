import pybullet as p

class WORLD:
    """
    Loads a world and a plane for the simulation
    """
    def __init__(self):
        p.loadSDF("world.sdf")
        self.plane_id = p.loadURDF("plane.urdf")