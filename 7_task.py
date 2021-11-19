def factorial(number):
    sum = 1
    for i in range(1, number + 1):
        sum *= i
        yield sum


n = int(input('Input number: '))
for el in factorial(n):
    print(el)
