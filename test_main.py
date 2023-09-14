from main import returnSecondValue

def test_sec():
    assert returnSecondValue("Lilly") == "i"
    assert returnSecondValue(["q", "r", "s"]) == "r"
