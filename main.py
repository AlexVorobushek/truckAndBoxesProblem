from BaseClasses.SetClass import Set
from BaseClasses.VectorClass import Vector

from BaseClasses.TruckClass import Truck
from BaseClasses.BoxClass import Box


def areBoxesIncluded(truck: Truck, new_boxes: Set):
    if len(new_boxes) == 1:
        return bool(truck.getWaysToIncludeBox(new_boxes[0]))
    for box in new_boxes:
        ways_to_include_box = truck.getWaysToIncludeBox(box)
        if not ways_to_include_box: continue
        for new_static_box in ways_to_include_box:
            new_truck = truck + new_static_box
            if areBoxesIncluded(new_truck, new_boxes-Set(box)): return True
    return False


if __name__ == "__main__":
    truck = Truck(
        size=Vector(2, 4, 6)
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
