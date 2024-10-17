s = input('Введите что угодно в строку: ')
a = s[:len(s)//2]
b = s[len(s)//2:]
if ('п' in a):
	i = a.replace('п', '*', )
print(i + b)
