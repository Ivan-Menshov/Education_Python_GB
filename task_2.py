class ZeroDivision(Exception):
    def __init__(self, text):
        self.text = text


try:
    a = float(input('введите делимое: '))
    b = float(input('введите делитель: '))
    if b == 0:
        raise ZeroDivision('Не делите на 0!')
    print(a/b)
except ZeroDivision as text:
    print(text)
