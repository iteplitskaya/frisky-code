_author_ = 'Теплицкая Ирина Владимировна'
print(_author_)
print()
print('Легкие задачи')
print()
print("Задача 1")
# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

a=int(input('Input number: '))
while a>0:
    print(a%10)
    a=a//10
    
print()
print('Задача 2')
# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!    

a=input('Input variable a: ')
b=input('Input variable b: ')
c=a
a=b
b=c
print('a=', a)
print('b=', b)

print()
print('Задача 3')
# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

a=int(input('Введите, пожалуйста, Ваш возраст: '))
if a>18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')
    
print()
print('Нормальные задачи')
print()
print('Задача 1')
# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.  

a=int(input('Input number: '))
max = 0
while a>0:
    digit = a%10
    a=a//10
    if digit>max:
        max = digit
print('Максимальная цифра в числе: ', max)

print()
print('Задача 2')
# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

a=input('Input variable a: ')
b=input('Input variable b: ')
c=a
a=b
b=c
print('a=', a)
print('b=', b)

print()
print('Задача 3')
# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4
import math
a=int(input('Введите коэффициент a: '))
b=int(input('Введите коэффициент b: '))
c=int(input('Введите коэффициент c: '))
d=b**2-4*a*c
sqrt=math.sqrt(d)
if d>=0:
    print('Корни квадратного уравнения:', (-b+sqrt)/(2*a), (-b-sqrt)/(2*a))
else:
    print("Уравнение решения не имеет")