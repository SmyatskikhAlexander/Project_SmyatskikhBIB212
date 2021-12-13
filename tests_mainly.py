from main import check, check_level2, check_level3, check_level5, check_level6, check_level7
def test_check_true():
    a = []
    a.append("пароль")
    assert check(a) == 1
def test_check_password():
    a = []
    a.append("Password")
    assert check(a) == 0
def test_check_space():
    a = []
    a.append("пароль ")
    assert check(a) == 0

def test_check_level2_true():
    a = []
    a.append("1946")
    assert check_level2(a) == 1
def test_check_level2_letters():
    a = []
    a.append("Тысяча девятьсот сорок шесть")
    assert check_level2(a) == 0
def test_check_level2_space():
    a = []
    a.append("1 9 4 6")
    assert check_level2(a) == 0

def test_check_level3_true():
    a = []
    a.append("1954")
    assert check_level3(a) == 1
def test_check_level3_inside():
    a = []
    a.append("195 4")
    assert check_level3(a) == 0
def test_check_level3_space():
    a = []
    a.append("19 46")
    assert check_level3(a) == 0

def test_check_level5_true():
    a = []
    a.append("292")
    assert check_level5(a) == 1
def test_check_level5_wrong():
    a = []
    a.append("166")
    assert check_level5(a) == 0
def test_check_level5_space():
    a = []
    a.append("2 9 2")
    assert check_level5(a) == 0

def test_check_level6_true():
    a = []
    a.append("Ботайте олимпиаду")
    assert check_level6(a) == 1
def test_check_level6_wrong():
    a = []
    a.append("0,651")
    assert check_level6(a) == 0
def test_check_level6_wrong2():
    a = []
    a.append("0.651")
    assert check_level6(a) == 0

def test_check_level7_true():
    a = []
    a.append("Alan Turing")
    assert check_level7(a) == 1
def test_check_level7_wrong_small_letters():
    a = []
    a.append("алан тьюринг")
    assert check_level7(a) == 0
def test_check_level7_numbers():
    a = []
    a.append("6584117114105110103")
    assert check_level7(a) == 0

def test_check_level7_nothing():
    a = []
    a.append("")
    assert check_level7(a) == 0