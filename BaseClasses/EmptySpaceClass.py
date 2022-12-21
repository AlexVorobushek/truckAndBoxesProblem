from BaseClasses.StaticSpaceClass import StaticSpace

from BaseClasses.VectorClass import Vector
from BaseClasses.SetClass import Set


class EmptySpace(StaticSpace):
    def __init__(self, size: Vector, coors: Vector) -> None:
        super().__init__(size, coors)

    def __add__(self, other: object):
        # CAN BE USED ONLY WHEN BOXES HAVE 5 COMMON PLANES\
        self_planes = self.repersentAsPlanes()
        other_planes = other.repersentAsPlanes()
        common_planes = self_planes & other_planes
        none_common_planes = (self_planes | other_planes)-common_planes
        orientation_of_common_face = none_common_planes[0].getOrientation()
        plane_of_common_face = list(filter(lambda plane: plane.getOrientation(
        ) == orientation_of_common_face, common_planes))[0]
        ans = (common_planes-Set(plane_of_common_face)) | none_common_planes
        return EmptySpace.initByPlanes(ans)
    
    @staticmethod
    def initByPlanes(planes: Set):
        staticSpace = StaticSpace.initByPlanes(planes)
        return EmptySpace(staticSpace.size, staticSpace.coors)
    
    def __repr__(self) -> str:
        return f"E(({self.size.x} {self.size.y} {self.size.z}) ({self.coors.x} {self.coors.y} {self.coors.z}))"
