class TacheClass:
    def __init__(self, name: str, r: int, c: int, d: int, p: int):
        self.name = name
        self.r = r
        self.c = c
        self.d = d
        self.p = p
        pass

    def __str__(self):
        return f"{self.name} {self.r} {self.c} {self.d} {self.p}"

# tache = TacheClass("t1", 1, 2, 3, 4)
