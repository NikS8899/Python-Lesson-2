# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

number = int(input("Введите число для обозначения промежутка: "))
result = list(range(-number,number + 1))
path = 'file.txt'
data = open(path, 'r')
sum = 1
for position in data:
    sum *= result[int(position)]
data.close()
print(result)
print(f'Сумма элементов на позиции равна = {sum}')

