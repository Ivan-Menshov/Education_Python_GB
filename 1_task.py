import sys
if len(sys.argv) < 4:
    print("Введите все аргументы! (выроботка,ставка ,премия)!")
else:
    print(float(sys.argv[1])*float(sys.argv[2])+float(sys.argv[3]))
