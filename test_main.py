# test test_main.py
from main import returnSecondValue


def test_sec():
    assert returnSecondValue("Lilly") == "i"
    assert returnSecondValue([1, 2, 3]) == 2
