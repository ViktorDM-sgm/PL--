def factorial(n):
	if n < 0:
		return 'Факториал не определен'
	elif n == 0 or n == 1:
		return 1
	else:
		i = 1
		for x in range (2, n+1):
			i *= x
		return i
	
z = int(input('Введите целое число: '))
print('Факториал числа', z, 'равен', factorial(z))