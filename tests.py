from main import arr, saveGame, loadGame, k

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


