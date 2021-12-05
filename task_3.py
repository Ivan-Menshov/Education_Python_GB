class Cells:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Cells(self.n + other.n)

    def __sub__(self, other):
        if (self.n - other.n) >= 0:
            return Cells(self.n - other.n)
        else:
            print('Err sub!')

    def __mul__(self, other):
        return Cells(self.n * other.n)

    def __truediv__(self, other):
        return Cells(self.n // other.n)

    def make_order(self, k):
        s = ''
        for i in range(self.n // k):
            s += '*' * k + '\n'
        s += '*' * (self.n % k) + '\n'
        return s

    def __str__(self):
        return f'{self.n}'


cell1 = Cells(15)
cell2 = Cells(7)

print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell2 - cell1)

print(cell1.make_order(4))
