import random
print("w- впeред "
      "s- назад"
      " d- впрaвo"
      " a- влево")


def create(size):
    '''Создаем игровое поле
    size - размер игрового поля
    Функция возвращает игровое поле'''
    arr = list()
    for i in range(size):
        arr.append([])
        for j in range(size):
            arr[i].append('')
    return arr

def print_arr(arr):
    '''Выводим игровое поле
    arr -  массив игрового поля
    Функция выводит игровое поле'''
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=' ')
        print()
def cls():
    '''Переносим строчку каждые 7 символов'''
    print('\n'*7)


def step(arr,x,y,m,l):
    '''Функция добавления точки игрока на поле
    arr - массив игрового поля; x, y - координаты игрока на поле; m, l - значения для шага
     Функция возвращает координаты игрока на поле'''
    arr[x][y]=' '
    x+=m
    y+=l
    arr[x][y]='*'
    return x,y

def tryStep(x,y,m,l):
    '''Функция проверяет невозможность шагнуть на преграду или за поле
    x, y - координаты игрока на поле; m, l - значения для шага
    Функция возвращает False пока игрок пытается выйти за карту или в преграду'''
    x+=m
    y+=l
    if x >= len(arr) or x < 0 or y >= len(arr) or y < 0 or arr[x][y] == '#':
        print ('Ты не пройдешь')
        return False
    else:
        cls()
        return True

def saveGame(k):
    '''Сохраняем нашу игру в текстовый файл'''
    fp = open("text.txt", "w")
    str1 = str(k)+'\n'
    str2 = str()
    for i in range(len(arr)):
        for j in range(len(arr)):
            str2 += str(arr[i][j])
    fp.write(str1)
    fp.write(str2)
    fp.close()

def loadGame():
    '''Загружаем нашу игру из текстового файла
    Функция возвращает координаты игрока на поле, выводит игровое поле'''
    x = 0
    y = 0
    fp = open("text.txt", "r")
    str1 = fp.readline()
    k = int(str1)
    str1 = fp.readline()
    for i in range(len(arr)):
        for j in range(len(arr)):
            arr[i][j] = str1[i*len(arr)+j]
            if arr[i][j] == '*':
                x = i
                y = j
    fp.close()
    return k, x, y

def Gen(arr):
    '''Заполняем наше игровое поле преградами
    Функция возвращает игровое поле с преградами'''
    for i in range(len(arr)):
        for j in range(len(arr)):
            if (random.randint(0, 10) < 5):
                arr[i][j] = "#"
            else:
                arr[i][j] = " "
    return arr

def start_point(arr):
    '''Проверка на пустое место, чтобы была возможность поставить стартовую точку'''
    flag = False
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == " ":

                arr[i][j] = str(0)
                flag = True
                break
        if flag:
            break


def possible(arr):
    '''Функция для волнового алгоритма'''
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == " ":
                return False
    return True

def wave(T):
    '''Проверяем возможность пути от старта до финиша с помощью алгоритма'''
    counter = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == str(T):
                if i - 1 > -1 and arr[i - 1][j] == " ":
                    arr[i - 1][j] = str(T + 1)
                    counter += 1
                if i + 1 < 7 and arr[i + 1][j] == " ":
                    arr[i + 1][j] = str(T + 1)
                    counter += 1
                if j - 1 > -1 and arr[i][j - 1] == " ":
                    arr[i][j - 1] = str(T + 1)
                    counter += 1
                if j + 1 < 7 and arr[i][j + 1] == " ":
                    arr[i][j + 1] = str(T + 1)
                    counter += 1
    return counter


def wave_alg(arr):
    '''Волновой алгоритм
    Алгоритм проверяет возможность дойти от старта до финиша'''
    start_point(arr)
    T = 0
    while (True):
        if wave(T) == 0:
            break
        T+=1
    return possible(arr)


arr = create(7)
arr = Gen(arr)
while(wave_alg(arr) == False):
    '''Генерируем игровое поле после работы волнового алгоритма'''
    Gen(arr)
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] != " " and arr[i][j] != "#":
            arr[i][j] = " "

k = 23

def rand_k(x, y):
    '''Ставим игрока на поле
    возвращает координаты игрока на поле'''
    x = random.randint(0,6)
    y = random.randint(0,6)
    return x, y
x = -1
y = -1
x , y = rand_k(x, y)
while arr[x][y] != ' ':
    x,y = rand_k(x, y)
else:
    arr[x][y] = '*'

xk = random.randint(0, 6)
yk = random.randint(0, 6)
arr[xk][yk]="$"
#print(xk, yk)
if __name__ == "__main__":
    print_arr(arr)
    while k > 0:


        if x == xk and y == yk:
            print("Ты победил!")
            break
        else:
            a = input()
            if a == 'save':
                saveGame(k)
                print("Игра сохранена.")
            elif a == "load":
                k, x, y = loadGame()
            else:
               if a == "a":
                   m = 0
                   l = -1
               elif a == "w":
                   m = -1
                   l = 0
               elif a =="s":
                   m = 1
                   l = 0
               elif a == "d":
                   m = 0
                   l = 1
               if (tryStep(x,y,m,l)):
                   x,y=step(arr,x,y,m,l)
                   k-=1
            if a != "save":
                print_arr(arr)
    else:
        print("(((")
