import custom_customs1, custom_customs2, pytest

def test_custom_customs1():
    file = "Day6/test_input.txt"
    result = custom_customs1.main(file) 
    assert result == 11

def test_custom_customs2():
    file = "Day6/test_input.txt"
    result = custom_customs2.main(file) 
    assert result == 6