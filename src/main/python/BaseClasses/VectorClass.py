class Vector:  # OrderedTripleElements
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __lt__(self, other: object):
        return all([
            self.x < other.x,
            self.y < other.y,
            self.z < other.z
        ])

    def __le__(self, other: object):
        return all([
            self.x <= other.x,
            self.y <= other.y,
            self.z <= other.z
        ])

    def __add__(self, other: object):
        return Vector(self.x+other.x, self.y+other.y, self.z+other.z)

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y and self.z == __o.z
    
    def __repr__(self):
        return "{" + f"{self.x} {self.y} {self.z}" + "}"


class Zero(Vector):
    def __init__(self) -> None:
        super().__init__(0, 0, 0)
