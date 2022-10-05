# First Exercise
"""
def Function():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    print(a+b)
Function()
"""

# Second Exercise
"""
while True:
    def function():
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        if a > b:
            print(a - b)
        else:
            print(b - a)
            print("Ваше число больше, чем нужно!")
    function()
"""
# Third Exercise
"""
while True:
    def function():
        c = int(input("Введите количество собак: "))
        b = c * 2
        a = b * 2
        d = a + b + c
        if (c<2):
            print("Меньше или равно двум быть не может")
        elif (c>1000):
            print("Больше или равно тысяче быть не может")
        else:
            print("Общее количество животных:", d)
    function()
"""
# Fourth Exercise
"""
while True:
    def function():
        n = int(input("\nВведите значение n = "))
        if (n<1):
            print("Меньше одного быть не может")
        elif (n>100):
            print("Больше ста быть не может")
        else:
            for i1 in range(1, n+1):
                print(i1, end=' ')
            print('\n')
            for i2 in reversed(range(1, n+1)):
                print(i2, end=' ')
    function()
"""
# Fifth Exercise
while True:
    def function():
        n = int(input("\nВведите значение n = "))
        if (n<1):
            print("Меньше одного быть не может")
        elif (n > 100):
            print("Больше ста быть не может")
        else:
            for i1 in reversed(range(1, n+1)):
                if(i1 % 2 != 0):
                    print(i1, end=' ')
    function()