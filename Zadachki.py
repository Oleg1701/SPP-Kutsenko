#1
x = int(input())
y = int(input())
print(x + y, x - y, x * y, x / y, end=' ')
#2
 x = int(input())
y = int(input())
print("Resultat", (abs(x) - abs(y)) / (1 + abs(x * y)))

#4
L = float(input('rebro = '))
print('Ploschad grani: {} \nPloschad bokovoi poverhnosti: {}\nObem: {}'.format(L ** 2, 6 * L ** 2, L ** 3))
#5.)
print(f'{(float(input()) + float(input())) / 2:.3f}')
#5.)
args = input('Enter your numbers separated by commas:')
print
'arithmetic average=', sum(map(abs, args)) / 2.
print
'geometric average=', reduce(lambda x, y: x * y, args) ** 0.5

#6)
A = float(input())
B = float(input())
import math

print(math.sqrt(A ** 2 + B ** 2))
print(0.5 * A * B)
#7)
x = float(input())
y = float(input())
z = float(input())
t = float(input())
print(x + z)
print(y + t)

#8)
import math

a = 3  # v 1
b = 4  # v 2
g = 10  # temp1
v = 15  # temp 2
c = a + b
o = (a * g + b * v) / c
print("Obyem=", c)
print("Temperatura =", o)
#9)
import math

r1 = 6
r2 = 1
r3 = 9
O = 1 / (1 / r1) + (1 / r2) + (1 / r3)
print("opir", O)

#10)
import math

h = 6
g = 9.8
o = math.sqrt(2 * h / g)
print("Padinna=", o)
#12.)
x = int(input())
s = x * 3
print("Plosha", s)

#13.)
import math

l = int(input())
g = 9.8
T = 6.28 * math.sqrt(l / 9.8)
print("Period", T)

#14.)
import math

m1 = int(input())
m2 = int(input())
r = int(input())
g = 9.8
F = g * m1 * m2 * r
print("Silla prityageniya=", F)

#15.)
import math

M = 5
k1 = 3
k2 = math.sqrt(math.pow(M, 2) - math.pow(k1, 2))
print("katet 2", k2)

#16.)
import math

l = int(input())
s = (l * l) / (4 * math.pi)
print("ploshja", s)

#17.)
import math

R = 20
r = int(input())
S = math.pi * (r - R)
print("Ploshja=", S)

#18.)
import math

r = int(input())
print("r=", r)
z1 = int(input())
print("z1=", z1)
z2 = int(input())
print("z2=", z2)
z3 = int(input())
print("z3", z3)
a = 2 * r * math.sin(z1)
b = 2 * r * math.sin(z2)
c = 2 * r * math.sin(z3)
print("1 storona", a)
print("2 storona", b)
print("3 storona", c)

#19.)
import math

v1 = int(input())
print("v1=", v1)
v2 = int(input())
print("v2=", v2)
a1 = int(input())
print("a1=", a1)
a2 = int(input())
print("a2=", a2)
s = int(input())
print("s=", s)
t = (-(v1 + v2) + math.sqrt((v1 + v2) * (v1 + v2) + 2 * (a1 + a2) * s)) / (a1 + a2)
print("Vremya", t)

#20.)
import math

c = int(input())
print("c=", c)
d = int(input())
print("d=", d)
x1 = (3 + math.sqrt(d)) / 2
x2 = (3 - math.sqrt(d)) / 2
x = math.fabs((abs(math.sin, 3)(c * abs(x1, 2) + d * abs(x2, 2) - c * d)) / (
    math.sqrt((c * abs(x1, 6) + d * abs(x2, 2) - x1) + 3.14))) + math.tan(c * abs(x1, 3) + d * abs(x2, 2) - x1)
print("x=", x)
#22.)
import math

a = int(input('a = '))
b = int(input('b = '))
A = int(input('A = '))

h = ((a - b) / 2) * math.tan(math.radians(A))
S = ((a + b) / 2) * h
print(round(S, 1))
input()

#23.)
import math

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

B = math.sqrt(c * b * (a + b + c) * (c + b - a)) / (c + b)
print("Bisektrisa=", B)
p = (a + b + c) / 2
print("p=", p)
P = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("Ploshja=", P)
V = 2 * P / 2
print("visota=", V)
M = math.sqrt(2 * (b * b + c * c) - a * a) / 2
print("mediana=", M)

#24.)
import math

x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))

d = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
print("distance=", d)

#25.)
import math

x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))
x3 = int(input('x3 = '))
y3 = int(input('y3 = '))
a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
c = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
p = (a + b + c) / 2.0
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("s=", s)
#26.)

def area():
    r = 13.7
    radian = float(input("Введите число радиан дуги:"))
    if radian <= 0:
        print("Неверный ввод")
    else:
        square = radian / 2 * (r * r)
        print(square)


if __name__ == '__main__':
    area()
#27.)
import math

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
A = math.acos((pow(b, 2) + pow(c, 2) - pow(a, 2)) / (2 * b * c))
B = math.acos((pow(a, 2) + pow(c, 2) - pow(b, 2)) / (2 * a * c))
G = math.acos((pow(b, 2) + pow(a, 2) - pow(c, 2)) / (2 * a * b))
print("Alfa=", A)
print("Gamma=", G)
print("Beta=", B)

#28)
import math

x = int(input('x = '))
a = 2 * pow(x, 4) - 3 * pow(x, 3) + 4 * pow(x, 2) - 5 * x + 6
print("a=", a)

#29.)
import math

x = int(input('x = '))
y = int(input('y = '))
a = 3 * pow(x, 2) * pow(y, 2) - 2 * x * pow(y, 2) - 7 * pow(x, 2) * y - 4 * pow(y, 2) + 15 * x * y + 2 * pow(x,
                                                                                                             2) - 3 * x + 10 * y + 6
print("A = ", a)
#30.)
import math

x = int(input('x = '))
A = 1 - 2 * x + 3 * pow(x, 2) - 4 * pow(x, 3)
B = 1 + 2 * x + 3 * pow(x, 2) + 4 * pow(x, 3)
print("A", A)
3
print("B", B)

import math

# 50

print("Задача 50")

a1 = float(input("Введите а1: "))
b1 = float(input("Введите b1: "))
c1 = float(input("Введите c1: "))
a2 = float(input("Введите a2: "))
b2 = float(input("Введите b2: "))
c2 = float(input("Введите c2: "))
eps = 0.0001

if math.fabs(a1 * b2 - a2 * b1) >= eps:
    x = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1)
y = (c1 * a2 - c2 * a1) / (a1 * b2 - a2 * b1)
print("x =", x)
print("y =", y)
else:
print("Не виконується умова")

# 51
a = int(input("Введите коэффициент a: "))
b = int(input("Введите коэффициент b: "))
c = int(input("Введите коэффициент c: "))

D = b * b - 4 * a * c

if D > 0:
    t1 = (-b) - math.sqrt(D) / 2 * a
t2 = (-b) + math.sqrt(D) / 2 * a
if t1 >= 0:
    x1 = math.sqrt(t1)
x2 = -math.sqrt(t1)
print("Корни уравнения: x1 =", x1, "x2 =", x2)
if t2 >= 0:
    x3 = math.sqrt(t2)
x4 = -math.sqrt(t2)
print("x3 = ", x3, "x4 = ", x4)
elif D == 0:
x1 = -b / 2 * a
x2 = -(-b / 2 * a)
print("Корни уравнения: x1 =", x1, "x2 =", x2)
elif D < 0:
print("Корни уравнения отсутствуют")
# 60
print("Задача 60")
x = float(input("Введите х: "))
y = float(input("Введите y: "))
u: float

menu = input("Выберите график:\n1 - a\n2 - б\n3 - в\n4 - г\n5 - д\n6 - е\n")
if menu == "1":
    if
-2 <= x <= -1 or 1 <= x <= 2 and 1 <= y <= 2: \
    u = 0;
else:
u = x
if menu == "2":
    if
y <= x / 2 and math.pow(y, 2) >= 1 - math.pow(x, 2):
u = -3
else:
u = math.pow(y, 2)
if menu == "3":
    if
(x * x) + (y - 1) * (y - 1) < 1 and y < (- x * x + 1):
u = x - y
else:
u = x * y + 7
if menu == "4":
    if
-1 <= x <= 0 or 0.3 <= x <= 1 and 0.3 <= y < 1:
u = math.pow(x, 2) - 1
else:
u = math.sqrt(math.fabs(x - 1))
if menu == "5":
    if
y > -x and ((x * x) + (y * y)) < 1 and y > x:
u = math.sqrt(math.fabs(math.pow(x, 2) - 1))
else:
u = x + y
if menu == "6":
    if
(x * x + y * y) <= 1 and (y - x) >= 0 and (y + x) >= 0:
u = x + y
else:
u = x - y
print("u =", u)

# 61
x = float(input("Введите десятичное число:"))
x_c = x
if x >= 0:
    x = math.floor(x)
x1 = math.floor(x)
if x <= 0:
    x = math.ceil(math.fabs(x))
x1 = math.ceil(x)
x_c1 = int(x_c)
print("Целая часть: ", x)
print("Округлённое до ближайшего целого: ", x1)
print("Число без дробной части:", x_c1)

# 70

print("Задача 70")
hour = int(input("Введите часы:"))
minute = int(input("Введите минуты:"))

full_circle = 720
t = 60 * hour + minute

sovp = round(full_circle * (round(t / (full_circle / 11)) + 1) / 11 - t)

curh = (hour * 30 + minute // 2) % 360
curm = minute * 6
x = (270 + curh) % 360
t1 = (360 + x - curm) % 180
print("Стрелки будут перпендикулярны через", t1 * 2 // 11, "минут(ы)")

print("Стрелки совпадут через ", sovp, "минут(ы)")

