from BaseClasses.SetClass import Set
from BaseClasses.TruckClass import Truck

from PythonJavaBridgeClass import PythonJavaBridge


def areBoxesIncluded(truck: Truck, new_boxes: Set):
    if len(new_boxes) == 1:
        return bool(truck.getWaysToIncludeBox(new_boxes[0]))
    for box in new_boxes:
        ways_to_include_box = truck.getWaysToIncludeBox(box)
        if not ways_to_include_box:
            continue
        for new_static_box in ways_to_include_box:
            new_truck = truck + new_static_box
            if areBoxesIncluded(new_truck, new_boxes-Set(box)):
                return True
    return False


def main():
    answer = areBoxesIncluded(
            PythonJavaBridge.getTrack(),
            PythonJavaBridge.getBoxes(),
        )
    PythonJavaBridge.print(str(answer))

if __name__ == "__main__":
    main()
