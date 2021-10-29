print('Что вы хотите найти?')
print('если площадь то введите:1')
print('если периметр введите:2')
d = 3

e = int(input())
if e <2:
    print("Периметр какой фигуры вам нужен?")
    print('если прямоугольника введите:1')
    print('если квадрата введите:2')
    w = int(input())
    if w <2:
        a = int(input('Введите a:'))
        b = int(input('Введите b:'))
        p = a*b
        print(p)
    else:
        a = int(input('Введите a:'))
        p = a**2

else:
    print("Периметр какой фигуры вам нужен?")
    print('если прямоугольника введите:1')
    print('если треугольника введите:2')
    print('если квадрата введите:3')
    what = int(input())
    if what < 3:
        if what <2:
            a = int(input('Введите a:'))
            b = int(input('Введите b:'))
            p = (a + b) * 2
            print(p)
        else:
            a = int(input('Введите a:'))
            b = int(input('Введите b:'))
            c = int(input('Введите c:'))
            p = a + b + c
            print(p)
    else:
        a = int(input('Введите a:'))
        p = 4 * a
        print(p)
