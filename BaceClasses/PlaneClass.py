class Plane:
    def __init__(self, x=None, y=None, z=None):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y and self.z == __o.z

    def get_orientation(self) -> str:
        if self.x != None:
            return "x"
        if self.y != None:
            return "y"
        return "z"

    def get_dimension(self) -> int:
        if self.x != None:
            return self.x
        if self.y != None:
            return self.y
        return self.z

    def __repr__(self) -> str:
        return f"{self.get_dimension()}{self.get_orientation()}"
    
    def __lt__(self, __o: object) -> bool:
        return self.get_dimension() < __o.get_dimension()
