# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

x = int(input("Введите номер четверти :"))
if x == 1:
    print("x=[1,+infinity], y=[1,+infinity]")
elif x == 2:
    print("x=[1,+infinity], y=[-infinity,-1]")
elif x == 3:
    print("x=[-infinity,-1], y=[-infinity,-1]")
elif x == 4:
    print("x=[-infinity,-1], y=[1,+infinity]")
else:
    print("Такой четверти не существует")
