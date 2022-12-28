from BaseClasses.StaticSpaceClass import StaticSpace

from BaseClasses.VectorClass import Vector


class StaticBox(StaticSpace):
    def __init__(self, size: Vector, coors: Vector, density: int = 0) -> None:
        super().__init__(size, coors)
        self.density = density

    def __contains__(self, other: object):
        return self.coors <= other.coors and other.coors + other.size <= self.coors + self.size
