import random
print("w- впeред "
      "s- назад"
      " d- впрaвo"
      " a- влево")


def create(size): # тут мы просто создаем массив 7 на 7
    arr = list()
    for i in range(size):
        arr.append([])
        for j in range(size):
            arr[i].append('')
    return arr
def print_arr(arr):  #заполнение массива пробелами
    for i in range(7):
        for j in range(7):
            print(arr[i][j], end=' ')
        print()
def cls():
    print('\n'*10)


def step(arr,x,y,m,l): #это функция шага, то есть просто заменяем  arr[i][j] на * (позицию персонажа)
    arr[x][y]=' '
    x+=m
    y+=l
    arr[x][y]='*'
    return x,y

def tryStep(x,y,m,l): #проверка на шаг если (мы выходим за пердел поля( при x>=7 или y>=7))
    x+=m
    y+=l
    if x >= 7 or x < 0 or y >= 7 or y < 0 or arr[x][y] == '#': #или же если arr[i][j]="#" то выдает ошибку
        print ('Ты не пройдешь')
        return False
    else:
        cls()
        return True

def saveGame(k):
    fp = open("text.txt", "w") # тут мы просто записываем наш массив в файл построчно
    str1 = str(k)+'\n'
    str2 = str()
    for i in range(7):
        for j in range(7):
            str2 += str(arr[i][j])
    fp.write(str1)
    fp.write(str2)
    fp.close()

def loadGame():  #тут мы просто выписываем  наш массив из файл построчно :)
    x = 0
    y = 0
    fp = open("text.txt", "r")
    str1 = fp.readline()
    k = int(str1)
    str1 = fp.readline()
    for i in range(7):
        for j in range(7):
            arr[i][j] = str1[i*7+j]
            if arr[i][j] == '*':
                x = i
                y = j
    fp.close()
    return k, x, y

def Gen(arr): #рандомное заполнение массив "#"
    for i in range(7):
        for j in range(7):
            if (random.randint(0, 10) < 5):
                arr[i][j] = "#"
            else:
                arr[i][j] = " "
    return arr
def start_point(arr):
    flag = False
    for i in range(7):
        for j in range(7):
            if arr[i][j] == " ":

                arr[i][j] = str(0)

                flag = True
                break
        if flag:
            break


def possible(arr):
    for i in range(7):
        for j in range(7):
            if arr[i][j] == " ":
                return False
    return True

def wave(T):   #волновой алгоритм нужен для проверки возможности пути от старта до финиша
    counter = 0
    for i in range(7):
        for j in range(7):
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
    start_point(arr)
    T = 0
    while (True):
        if wave(T) == 0:
            break
        T+=1
    return possible(arr)


arr = create(7)
arr = Gen(arr)
while(wave_alg(arr) == False):  # ну тут изходя из волнового алгоритма делаем так чтобы игрок мог дойти до финиша
    Gen(arr)
for i in range(7):
    for j in range(7):
        if arr[i][j] != " " and arr[i][j] != "#":
            arr[i][j] = " "

k = 23

def rand_k(x, y):	# вот тут мы ставим игрока на поле
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

xk = random.randint(0, 6) # тут ставим финиш на поле
yk = random.randint(0, 6)
arr[xk][yk]="$"
#print(xk, yk)
if __name__ == "__main__":
    print_arr(arr)
    while k > 0:


        if x == xk and y == yk: # тут провеврка на победу
            print("Ты победил!")
            break
        else:		# а это управление тип в зависимости от того что мы нажали переменным присваиваеться переменным
            # делаем ход
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
