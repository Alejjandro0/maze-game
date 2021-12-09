from main import arr, saveGame, loadGame, k

def test_dada():
    old_arr = arr.copy()
    saveGame(k)
    loadGame()
    assert old_arr == arr



