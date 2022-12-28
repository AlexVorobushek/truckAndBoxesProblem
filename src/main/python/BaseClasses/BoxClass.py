from BaseClasses.SpaceClass import Space
from BaseClasses.StaticBoxClass import StaticBox
from BaseClasses.EmptySpaceClass import EmptySpace

from BaseClasses.VectorClass import Vector
from BaseClasses.SetClass import Set


class Box(Space):
    def __init__(self, size: Vector, density: int = 0) -> None:
        super().__init__(size)
        self.density = density

    def possibleSizesGenerator(self) -> Vector:
        for size in Set(
            Vector(self.size.x, self.size.y, self.size.z),
            Vector(self.size.x, self.size.z, self.size.y),
            Vector(self.size.y, self.size.x, self.size.z),
            Vector(self.size.y, self.size.z, self.size.x),
            Vector(self.size.z, self.size.y, self.size.x),
            Vector(self.size.z, self.size.x, self.size.y),
        ):
            yield size

    def getPossibleStaticBoxesInEmptySpace(self, empty_space: EmptySpace) -> Set:
        result_spaces = Set()
        for size in self.possibleSizesGenerator():
            if not (size <= empty_space.size):
                continue
            for coors in Set(
                Vector(0, 0, 0),

                Vector(empty_space.size.x-size.x, 0, 0),
                Vector(0, empty_space.size.y-size.y, 0),
                Vector(0, 0, empty_space.size.z-size.z),

                Vector(0, empty_space.size.y-size.y, empty_space.size.z-size.z),
                Vector(empty_space.size.x-size.x, 0, empty_space.size.z-size.z),
                Vector(empty_space.size.x-size.x, empty_space.size.y-size.y, 0),

                Vector(
                    empty_space.size.x-size.x,
                    empty_space.size.y-size.y,
                    empty_space.size.z-size.z),
            ):
                result_spaces.add(
                    StaticBox(size, coors+empty_space.coors, self.density)
                )
        return result_spaces
