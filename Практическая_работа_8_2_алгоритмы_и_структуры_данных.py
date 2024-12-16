#Практическая работа_8 (2)
def znach_10(n):
    return f"{n:o}".zfill(10)
n = int(input("Введите неотрицательное целое число: "))
znach_8 = znach_10(n)
print(f"Восьмеричный код: {znach_8}")