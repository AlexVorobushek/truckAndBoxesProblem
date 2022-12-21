from DataTypes.SetClass import Set
from DataTypes.Vector import Zero
from DataTypes.Vector import Vector

from BaceClasses.SpaceClass import Space
from BaceClasses.BoxClass import Box


def boxLocationsInTruck(box: Box, truck: Space):
    result_spaces = Set()
    for size in box.size.combinations():
        if not (size <= truck.size):
            continue
        for coors in Set(
            Vector(0, 0, 0),

            Vector(truck.size.x-size.x, 0, 0),
            Vector(0, truck.size.y-size.y, 0),
            Vector(0, 0, truck.size.z-size.z),

            Vector(0, truck.size.y-size.y, truck.size.z-size.z),
            Vector(truck.size.x-size.x, 0, truck.size.z-size.z),
            Vector(truck.size.x-size.x, truck.size.y-size.y, 0),

            Vector(
                truck.size.x-size.x,
                truck.size.y-size.y,
                truck.size.z-size.z),
        ):
            result_spaces.add(Space(size, coors+truck.coors))
    return result_spaces


def getNewMiniSpaces(truck: Space, boxes: list) -> Set:
    planes = truck.repersentAsPlanes()
    for box in boxes:
        planes |= box.repersentAsPlanes()

    x_planes = sorted(
        filter(lambda plane: plane.get_orientation() == "x", planes))
    y_planes = sorted(
        filter(lambda plane: plane.get_orientation() == "y", planes))
    z_planes = sorted(
        filter(lambda plane: plane.get_orientation() == "z", planes))

    dissected_spase = Set()
    for xi1 in range(0, len(x_planes)-1):
        for yi1 in range(0, len(y_planes)-1):
            for zi1 in range(0, len(z_planes)-1):
                dissected_spase.add(
                    Space.initByPlanes([
                        x_planes[xi1],
                        x_planes[xi1+1],
                        y_planes[yi1],
                        y_planes[yi1+1],
                        z_planes[zi1],
                        z_planes[zi1+1],
                    ])
                )
    only_mini_spaces = Set()
    for mini_space in dissected_spase:
        for box in boxes:
            if mini_space in box:
                break
        else:
            only_mini_spaces.add(mini_space)

    return only_mini_spaces


# превращает из одного решения mini_spaces множество решений
def getCombsOfNewSpaces(mini_spaces: Set) -> Set:
    answers = Set()
    mini_spaces_len = len(mini_spaces)
    for i in range(0, mini_spaces_len-1):
        for j in range(i+1, mini_spaces_len):
            if len(mini_spaces[i].repersentAsPlanes() & mini_spaces[j].repersentAsPlanes()) == 5:
                answers |= getCombsOfNewSpaces(
                    (mini_spaces - Set(mini_spaces[i], mini_spaces[j])).add(mini_spaces[i]+mini_spaces[j]))
    return answers if answers else Set(mini_spaces)


#когда коробки поставлены определенным образом и нужно проверить, можно ли поставить еще одну. ф-я покажет все варианты расположения
def BoxIncludeToFilledTruckWays(truck, static_boxes, next_box):
    result_boxes = Set()
    for divided_space in getCombsOfNewSpaces(getNewMiniSpaces(truck, static_boxes)):
        for mini_truck in divided_space:
            result_boxes |= boxLocationsInTruck(next_box, mini_truck)
    return result_boxes


def areBoxesIncluded(truck, new_boxes: Set, static_boxes:Set=Set()):
    if len(new_boxes) == 1:
        return bool(BoxIncludeToFilledTruckWays(truck, static_boxes, new_boxes[0]))
    for box in new_boxes:
        ways_to_stay_next_box = BoxIncludeToFilledTruckWays(truck, static_boxes, box)
        if not ways_to_stay_next_box: continue
        for new_const_box in ways_to_stay_next_box:
            if areBoxesIncluded(truck, new_boxes-Set(box), static_boxes.add(new_const_box)): return True
    return False


if __name__ == "__main__":
    truck = Space(
        size=Vector(2, 4, 6),
        coors=Zero()
    )
    boxes = Set(
        Box(
            size=Vector(1, 2, 6)
        ),
        Box(
            size=Vector(2, 2, 3)
        ),
        Box(
            size=Vector(1, 4, 3)
        ),
        Box(
            size=Vector(1, 2, 3)
        ),
        Box(
            size=Vector(1, 2, 3)
        ),
    )

    box1 = Box(
        size=Vector(3, 1, 1)
    )

    print(areBoxesIncluded(truck, boxes))
