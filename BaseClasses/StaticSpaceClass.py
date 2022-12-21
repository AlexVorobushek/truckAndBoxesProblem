from BaseClasses.SpaceClass import Space
from BaseClasses.PlaneClass import Plane

from BaseClasses.VectorClass import Vector
from BaseClasses.SetClass import Set


class StaticSpace(Space):
    def __init__(self, size: Vector, coors: Vector) -> None:
        super().__init__(size)
        self.coors = coors

    def repersentAsPlanes(self) -> Set:
        return Set(
            Plane(x=self.coors.x),
            Plane(y=self.coors.y),
            Plane(z=self.coors.z),
            Plane(x=self.coors.x+self.size.x),
            Plane(y=self.coors.y+self.size.y),
            Plane(z=self.coors.z+self.size.z),
        )

    @staticmethod
    def initByPlanes(planes: Set) -> object:
        x_dimension = sorted(map(lambda plane: plane.getDimension(), filter(
            lambda plane: plane.getOrientation() == "x", planes)))
        y_dimension = sorted(map(lambda plane: plane.getDimension(), filter(
            lambda plane: plane.getOrientation() == "y", planes)))
        z_dimension = sorted(map(lambda plane: plane.getDimension(), filter(
            lambda plane: plane.getOrientation() == "z", planes)))

        return StaticSpace(
            Vector(
                x_dimension[1] - x_dimension[0],
                y_dimension[1] - y_dimension[0],
                z_dimension[1] - z_dimension[0],
            ),
            Vector(
                x_dimension[0],
                y_dimension[0],
                z_dimension[0],
            ),
        )

    def __eq__(self, other: object) -> bool:
        return self.repersentAsPlanes() == other.repersentAsPlanes()
    
    def __repr__(self) -> str:
        return f"S(({self.size.x} {self.size.y} {self.size.z}) ({self.coors.x} {self.coors.y} {self.coors.z}))"
