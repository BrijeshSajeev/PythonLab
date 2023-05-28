class Ex:
    __slots__ = ["a", "b"]

    def __init__(self, a, b):
        self.a = a
        self.b = b

    # def __str__(self) -> str:
    #     print(self.a+self.b)


a = Ex(20, 89)
print(a.__slots__)
