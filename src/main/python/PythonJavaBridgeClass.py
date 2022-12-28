from BaseClasses.SetClass import Set
from BaseClasses.VectorClass import Vector

from BaseClasses.TruckClass import Truck
from BaseClasses.BoxClass import Box
from BaseClasses.StaticBoxClass import StaticBox

import json


class PythonJavaBridge:
    @staticmethod
    def getTrack() -> Truck:
        with open("..\pythonJavaCommonDirectory\TrackParams.json") as file:
            serialized_data = file.read()
        data = json.loads(serialized_data)
        truck = Truck(
            Vector(*data["size"]),
            Set(
                *[
                    StaticBox(
                        Vector(*item["size"]),
                        Vector(*item["coors"]),
                        item["density"]
                    ) for item in data["staticBoxes"]
                ]
            )
        )
        return truck

    @staticmethod
    def getBoxes() -> Set():
        with open("..\pythonJavaCommonDirectory\BoxesParams.json") as file:
            serialized_data = file.read()
        data = json.loads(serialized_data)
        boxes = Set(
            *[
                Box(
                    Vector(*item["size"]),
                    item["density"]
                ) for item in data
            ]
        )
        return boxes

    @staticmethod
    def print(text) -> None:
        with open("..\pythonJavaCommonDirectory\pythonResult.txt", "w") as file:
            file.write(text)
