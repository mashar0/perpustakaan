class H:

    def __init__(self, x, y):
        self.x, self.y = x, y

    def perkenalkan(self):
        print(f"Aku mempunyai tinggi {self.x} dan lebar {self.y}")

g = H(100,20)
g.perkenalkan()
