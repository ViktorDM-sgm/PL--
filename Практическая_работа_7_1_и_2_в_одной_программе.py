x = []
for i in range(10):#Не указана длина массива
    x.append(int(input('Задайте значения для массива: ')))
    t = 0
    for s in range(len(x)):
        if s % 2 != 0:
            t += x[s]
    m = 1
    for u in range(len(x)):
        if u % 2 == 0:
            m *= x[u]
print('Произведение чисел из массива, с нечетными номерами: ', m)
print('Сумма чисел из массива, с четными номерами: ', t)
mini = x.index(min(x))
maxi = x.index(max(x))
x[mini], x[maxi] = x[maxi], x[mini]
print('Полученный массив после перестановки максимального и минимального значений: ', x)