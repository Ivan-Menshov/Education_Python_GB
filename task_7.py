class Complex:
    def __init__(self, i, j):
        self.a = i
        self.b = j

    def __str__(self):
        return f'{self.a}+{self.b}j'

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)


my_number1 = Complex(1, 2)
my_number2 = Complex(3, -1)
print(my_number1 + my_number2)
print(my_number1 * my_number2)
