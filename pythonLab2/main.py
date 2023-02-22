import numpy as np
import random

f = open('C:\\Users\\Molniya\\Desktop\\output.txt', 'w') #Открытие файла для записи

print("Введите количеств сторок матрицы: ")
N = int(input()) # вводим переменную содержащую количество строк матрицы
print("Введите количеств столбцов матрицы: ")
M = int(input())# вводим переменную содержащую количество столбцов матрицы
print("Введите границы диапазона для автоматического заполнения матрицы: ")
l = int(input()) # вводим переменную левую границу диапазона
r = int(input()) # вводим переменную правую границу диапазона
aver = 0 # переменная содержащая сумму элементов строки
list = [] # объявляем список
A = np.eye(N, M) #объявляем единичную матрицу с N строками и M столбцами, используется библиотека numpy

f.write("Исходные данные: " + '\n')

for i in range(N): # с помощью цикла for проходимся по матрице
    for j in range(M):
        A[i][j] = random.randint(l, r) #заменяем каждый элементы единичной матрицы рандомными значекниями
        f.write(str(A[i][j]) + '\t')#записываем элементы в файл
        aver += A[i][j] #суммируем элементы строки
    list.append(aver/M) #добавляем в наш список среднее значение строки
    aver = 0 #обнуляем переменную с суммой элементов строки
    f.write('\n')
f.write('\n')

B = float("{0:.2f}".format(min(list))) #при помощи функции min находим минимальное значение из средних значений каждой строки и округляем его до 2 знаков после запятой

f.write("Результат обработки: " + '\n')
f.write(str(B)) # записываем результат в файл
f.close() # закрываем файл
print("Программа успешно завершила работу, пожалуйста, проверьте выходной файл!")
