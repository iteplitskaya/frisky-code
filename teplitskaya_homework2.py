_author_ = 'Теплицкая Ирина Владимировна'
print(_author_)
print()
print('Легкие задачи')
print()
print("Задача 1")

#Дан список фруктов.Напишите программу, выводящую фрукты в виде нумерованного списка, выровненного по правой стороне.
#Пример:
#Дано: [[яблоко], банан, "киви", "арбуз"]
#Вывод:
#1. яблоко
#2. банан
#3. киви
#4. арбуз
#Подсказка: воспользоваться методом .format()


l=['дыня', 'груша', 'апельсин', 'слива']
for i in range(4):
    print(("№{}. ".format(i+1)+l[i]).rjust(20))

print()
print("Задача 2")

#Даны два произвольные списка. Удалите из первого списка элементы, присутствующие во втором списке.

l=['дыня', 3, 'a', 5, 7, 9]
m=[8, 'дыня', 6, 'b', 5, 4, 9]
set_l = set(l)
set_m = set(m)
print(set_l-set_l.intersection(set_m))

print()
print("Задача 3")

#Дан произвольный список из целых чисел.Получите НОВЫЙ список из элементов исходного, выполнив следующие условия: если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

l=[1, 4, 6, 7, 9, 12, 34, 56, 900, 33, 11]
l_new = list()
for i in range(10):
    if l[i]%2==0:
        l_new.append(l[i]/4)
    else:
        l_new.append(l[i]*2)
        
print(l_new)