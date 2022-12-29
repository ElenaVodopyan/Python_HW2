# Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

first = input('Введите первую строку ')
second = input('Введите вторую строку ')
for s in first:
    print(f'{s} - {second.count(s)}')
