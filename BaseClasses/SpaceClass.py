from BaseClasses.PlaneClass import Plane

from BaseClasses.VectorClass import Vector
from BaseClasses.SetClass import Set


class Space:
    def __init__(self, size: Vector) -> None:
        self.size = size

    def repersentAsPlanes(self) -> Set:
        return Set(
            Plane(x=0),
            Plane(y=0),
            Plane(z=0),
            Plane(x=self.size.x),
            Plane(y=self.size.y),
            Plane(z=self.size.z),
        )
