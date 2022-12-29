# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

n = int(input('Введите число '))
list = []
for s in range(-n, n+1):
    list.append(s)

list = list[len(list)-2:len(list):1]+list[0:len(list)-2:1]    
print(list)