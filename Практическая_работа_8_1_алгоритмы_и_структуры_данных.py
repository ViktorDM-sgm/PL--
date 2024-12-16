#Практическая работа_8 (1)
def s_pryam(x, y):
    return x * y
def s_treug(x, y):
    return 0.5 * x * y
def s_cheug(x, y, z, t):
    s_pryamoug = s_pryam(x, y)
    s_treugol = s_treug(y, z)
    s_treugol_2 = s_treug(x, t)
    return s_pryamoug + s_treugol + s_treugol_2
x = float(input("Введите длину стороны x: "))
y = float(input("Введите длину стороны y: "))
z = float(input("Введите длину стороны z: "))
t = float(input("Введите длину стороны t: "))
S = s_cheug(x, y, z, t)
print(f"Площадь четырехугольника: {S}")