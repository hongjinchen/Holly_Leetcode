class OrderedStream:
    def __init__(self, n: int):
        self.data, self.ptr = [None] * n, 0

    def insert(self, idKey: int, value: str) -> list[str]:
        # insert
        listPlace = idKey
        self.data[listPlace - 1] = value
        reasult = []
        while self.ptr < len(self.data) and self.data[self.ptr]:
            reasult.append(self.data[self.ptr])
            self.ptr += 1
        return reasult
