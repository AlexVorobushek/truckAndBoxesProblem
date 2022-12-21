from DataTypes.SetClass import Set
from DataTypes.Vector import Vector

from BaceClasses.PlaneClass import Plane

class Space:  # need to rename to Space
    def __init__(self, size: Vector, coors: Vector) -> None:
        self.size = size
        self.coors = coors

    def __eq__(self, other: object) -> bool:
        return self.repersentAsPlanes() == other.repersentAsPlanes()

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
    def initByPlanes(planes: list) -> object:
        x_dimension = sorted(map(lambda plane: plane.get_dimension(), filter(
            lambda plane: plane.get_orientation() == "x", planes)))
        y_dimension = sorted(map(lambda plane: plane.get_dimension(), filter(
            lambda plane: plane.get_orientation() == "y", planes)))
        z_dimension = sorted(map(lambda plane: plane.get_dimension(), filter(
            lambda plane: plane.get_orientation() == "z", planes)))

        return Space(
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

    def __contains__(self, other: object):
        return self.coors <= other.coors and other.coors + other.size <= self.coors + self.size

    def __add__(self, other: object):
        # CAN BE USED ONLY WHEN BOXES HAVE 5 COMMON PLACES\
        self_planes = self.repersentAsPlanes()
        other_planes = other.repersentAsPlanes()
        common_places = self_planes&other_planes
        none_common_places = (self_planes|other_planes)-common_places
        orientation_of_common_face = none_common_places[0].get_orientation()
        place_of_common_face = list(filter(lambda place: place.get_orientation()==orientation_of_common_face, common_places))[0]
        ans = (common_places-Set(place_of_common_face)) | none_common_places
        return Space.initByPlanes( ans )

    def __repr__(self) -> str:
        return f"(({self.size.x} {self.size.y} {self.size.z}) ({self.coors.x} {self.coors.y} {self.coors.z}))"
