# Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def faktorial(n):
    res = 1 
    for i in range(2, n + 1):
        res = res * i
    return res

n = int(input('Введите число '))
for i in range(1, n + 1):
    print(faktorial(i))
