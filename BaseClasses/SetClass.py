class Set:
    def __init__(self, *elems) -> None:
        self.list = []
        for elem in elems:
            self.add(elem)

    def add(self, elem):
        if elem not in self:
            self.list.append(elem)
        return self

    def __len__(self):
        return len(self.list)

    def __iter__(self):
        for i in self.list:
            yield i

    def __eq__(self, __o: object) -> bool:
        return len(self & __o) == len(self | __o)

    def __or__(self, __o: object):
        ans = Set(*(self.list + __o.list))
        return ans

    def __and__(self, __o: object) -> object:
        ans = Set()
        for item in self:
            if item in __o:
                ans.add(item)
        return ans

    def __contains__(self, elem) -> bool:
        for item in self.list:
            if elem == item:
                return True
        return False

    def __sub__(self, __o: object):
        ans = Set()
        for item in self:
            if item not in __o:
                ans.add(item)
        return ans

    def __repr__(self) -> str:
        return str(self.list)

    def __getitem__(self, index):
        return self.list[index]

    def __bool__(self):
        return bool(self.list)
