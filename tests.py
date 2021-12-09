from main import arr, saveGame, loadGame, k, x, y, possible, tryStep, start_point

def test_saveload():
    old_arr = arr.copy()
    saveGame(k)
    loadGame()
    assert old_arr == arr

def test_pregrada():
    pregrada1=0
    pregrada=arr.count('#')
    saveGame(k)
    file = open("text.txt", "r")
    if '#' in file:
        pregrada1+=1
    assert pregrada==pregrada1

#def test_tryStep():
#    x=1
#    y=1
#    arr[x][y+1]='*'
#    arr[x][y]='#'
#    if y-1:
#        return False
#    tryStep(x,y,m,l)
#    assert [return False]

def test_possible():
    arr[x][y]=' '
    assert not possible(arr)

def test_tryStep():
    x=10
    y=10
    m=0
    l=0
    assert not tryStep(x, y, m, l)
    x=6
    y=5
    m=0
    l=1
    arr[x+m][y+l]='#'
    assert not tryStep(x, y, m, l)
