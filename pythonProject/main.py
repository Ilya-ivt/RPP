
import random

a = 0
listA = [] #Объявление списка
listB = []

def update(): #Основная логика
    for i in listA: # с помощью цокла for проходимся по списку A
        eA = listA.count(i) #Присваиваем в переменную eA количество вхождений текущего элемента
        if eA >= 2:#Проверяем, чтобы кол. вхождений было больше, либо равно 2
            for j in listB: # с помощью цокла for проходимся по списку B
                if j == i: #Если значение элемента списка B равно значению элемента списка A
                    eB = listB.count(j) #Присваиваем в переменную eB количество вхождений текущего элемента
                    if eB >= 2: #Проверяем, чтобы кол. вхождений было больше, либо равно 2
                        listA.remove(i) #Удаляем элемент с этим значением из списка A
    return listA #Возвращаем измененный список A

def userInput(): #Функция ввода пользователя
    while True:
        try:
            a = int(input("Пожалуйста выберите, каким образом вы хотели бы заполнить список: вручную (введите 0) или автоматически случайными "
        "числами (введите 1): "))
        except ValueError:
            print("Пожалуйста введите целое число из предложенных вариантов")
        else:
            if ((a != 0) and (a != 1)): #обработка ошибки ввода
                print("Пожалуйста введите целое число из предложенных вариантов")
            else:
                return a
                break

a = userInput()

if a == 0:  #Если спик заполняется вручную
    while True:
        try:
            nA = int(input("Пожалуйста введите количество элементов списка A: "))
            nB = int(input("Пожалуйста введите количество элементов списка B: "))
        except ValueError:
            print("Пожалуйста введите целое положительное число")
        else:
            if (nA <= 0):
                print("Пожалуйста введите целое положительное число")

            else:
                print("Пожалуйста введите элементы списка A: ")

                for i in range(nA):
                    while True:
                        try:
                            e = int(input())
                        except ValueError:
                            print("Пожалуйста введите целое число")
                        else:
                            listA.append(e) # добавление элементов в список
                            break
                if (nB <= 0):
                    print("Пожалуйста введите целое положительное число")

                else:
                    print("Пожалуйста введите элементы списка B: ")

                    for i in range(nB):
                        while True:
                            try:
                                e = int(input())
                            except ValueError:
                                print("Пожалуйста введите целое число")
                            else:
                                listB.append(e)
                                break

                print("Список A до преобразования:")
                print(listA)
                print("Список B до преобразования:")
                print(listB)
                listA = update()
                print("Список A после преобразования:")
                print(listA)
                break


else: #Если спик заполняется атоматически
    while True:
        try:
            nA = int(input("Пожалуйста введите количество элементов списка A: "))
            nB = int(input("Пожалуйста введите количество элементов списка B: "))
        except ValueError:
            print("Пожалуйста введите целое положительное число")
        else:
            if (nA <= 0):
                print("Пожалуйста введите целое положительное число")
            else:
                while True:
                    try:
                        lA = int(input("Пожалуйста введите значение левой границы диапазона для генерации случайных чисел списка A: "))
                        rA = int(input("Пожалуйста введите значение правой границы диапазона для генерации случайных чисел списка A: "))
                    except ValueError:
                        print("Пожалуйста введите целое число")
                    else:
                        for i in range(nA):
                            e = random.randint(lA, rA) #Используется рандомайзер, для заполнения, в пределах от lA до rA

                            listA.append(e)
                        break
                if (nB <= 0):
                    print("Пожалуйста введите целое положительное число")
                else:
                    while True:
                        try:
                            lB = int(input(
                                "Пожалуйста введите значение левой границы диапазона для генерации случайных чисел списка B: "))
                            rB = int(input(
                                "Пожалуйста введите значение правой границы диапазона для генерации случайных чисел списка B: "))
                        except ValueError:
                            print("Пожалуйста введите целое число")
                        else:
                            for i in range(nB):
                                e = random.randint(lB, rB)

                                listB.append(e)
                            break


                print("Список A до преобразования:")
                print(listA) #Вывод списка
                print("Список B до преобразования:")
                print(listB)

                listA = update()
                print("Список A после преобразования:")
                print(listA)
        break


