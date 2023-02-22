import csv
import datetime
from pathlib import Path

def userInput(): #Функция ввода пользователя
    while True:
        try:
            a = int(input("Введите 0, если Вы хотите узнать количество файлов в директории, или введите 1 если хотете обработать CSV-файл: "))
        except ValueError:
            print("Пожалуйста введите целое число из предложенных вариантов")
        else:
            if ((a != 0) and (a != 1)): #обработка ошибки ввода
                print("Пожалуйста введите целое число из предложенных вариантов")
            else:
                return a
                break

a = userInput()


if (a == 0):
    path = input("Пожалуйста введите полный путь до папки или директорию: ")
    directory = Path(path)

    if not directory.is_dir():
        print(ValueError(f"[{directory}] не существует или не является директорией!"))
    else:
        print(f"В папке (директории) [{path}] находится {len(list(directory.iterdir()))} объектов")
        #print(f"В папке (директории) [{path}] и в её папках (поддиректориях) находится {len(list(directory.rglob('*')))} объектов")


elif(a == 1):
    fI = open("C:\\Users\\Molniya\\Desktop\\data2.csv", 'r')

    reader = csv.DictReader(fI, fieldnames=None, restkey=None, restval=None, dialect="excel") #переменная для чтения файла формата csv

    l = list(reader) #список содержащий данные из файла

    print(l)

    sSL = sorted(l, key=lambda d: str(d['Assessment description'])) # Сортировка по строковомы значению
    nSL = sorted(l, key=lambda d: str(d['N']), reverse=True) #Сортировка по числовому значению

    print(sSL)
    print(nSL)

    tSL = []

    # Вывод информации по времени
    for line in l:
        time = datetime.datetime.strptime(line['Time'], '%H:%M')
        if time.hour > 14:
            tSL.append(line)


    with open("C:\\Users\\Molniya\\Desktop\\output.csv", 'w', newline='') as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames = reader.fieldnames) #переменная для записи данных в файл
        writer.writeheader()

        for row in sSL:
            writer.writerow(row)

        for row in nSL:
            writer.writerow(row)

        for row in tSL:
            writer.writerow(row)
