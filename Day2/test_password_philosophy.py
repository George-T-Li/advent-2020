import password_philosophy1, password_philosophy2, pytest

def test_password_philosophy1():
    file = "Day2/test_input.txt"
    result = password_philosophy1.main(file) 
    assert result == 2

def test_password_philosophy2():
    file = "Day2/test_input.txt"
    result = password_philosophy2.main(file)
    assert result == 1