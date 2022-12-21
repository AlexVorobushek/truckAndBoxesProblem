from BaseClasses.SpaceClass import Space
from BaseClasses.EmptySpaceClass import EmptySpace
from BaseClasses.StaticBoxClass import StaticBox

from BaseClasses.VectorClass import Vector
from BaseClasses.SetClass import Set


class Truck(Space):
    def __init__(self, size: Vector, static_boxes: Set = Set()) -> None:
        super().__init__(size)
        self.static_boxes = static_boxes

    def __add__(self, static_box: StaticBox):
        return Truck(self.size, self.static_boxes.add(static_box))

    # split void space into many base empty spaces
    def __splitAllEmptySpaceIntoManyEmptySpaces(self) -> Set:
        planes = self.repersentAsPlanes()
        for box in self.static_boxes:
            planes |= box.repersentAsPlanes()

        x_planes = sorted(
            filter(lambda plane: plane.getOrientation() == "x", planes))
        y_planes = sorted(
            filter(lambda plane: plane.getOrientation() == "y", planes))
        z_planes = sorted(
            filter(lambda plane: plane.getOrientation() == "z", planes))

        dissected_spase = Set()
        for xi1 in range(0, len(x_planes)-1):
            for yi1 in range(0, len(y_planes)-1):
                for zi1 in range(0, len(z_planes)-1):
                    dissected_spase.add(
                        EmptySpace.initByPlanes([
                            x_planes[xi1],
                            x_planes[xi1+1],
                            y_planes[yi1],
                            y_planes[yi1+1],
                            z_planes[zi1],
                            z_planes[zi1+1],
                        ])
                    )
        only_empty_spaces = Set()
        for mini_space in dissected_spase:
            for box in self.static_boxes:
                if mini_space in box:
                    break
            else:
                only_empty_spaces.add(EmptySpace(mini_space.size, mini_space.coors))

        return only_empty_spaces

    # превращает из одного решения mini_spaces множество решений
    @staticmethod
    def __getPossibleCombsOfEmptySpaces(empty_spaces) -> Set:
        answers = Set()
        empty_spaces_len = len(empty_spaces)
        for i in range(0, empty_spaces_len-1):
            for j in range(i+1, empty_spaces_len):
                if len(empty_spaces[i].repersentAsPlanes() & empty_spaces[j].repersentAsPlanes()) == 5:
                    answers |= Truck.__getPossibleCombsOfEmptySpaces(
                        (empty_spaces - Set(empty_spaces[i], empty_spaces[j])).add(empty_spaces[i]+empty_spaces[j]))
        return answers if answers else Set(empty_spaces)

    def getPossibleCombsOfEmptySpaces(self) -> Set:
        return Truck.__getPossibleCombsOfEmptySpaces(self.__splitAllEmptySpaceIntoManyEmptySpaces())

    def getWaysToIncludeBox(self, next_box) -> Set:
        result_static_boxes = Set()
        for divided_space in self.getPossibleCombsOfEmptySpaces():
            for empty_space in divided_space:
                result_static_boxes |= next_box.getPossibleStaticBoxesInEmptySpace(empty_space)
        return result_static_boxes
