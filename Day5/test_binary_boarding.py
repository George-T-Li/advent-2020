import binary_boarding1, pytest

def test_get_row():
    seat = "FBFBBFFRLR"
    result = binary_boarding1.get_row(seat) 
    assert result == 44

def test_get_col():
    seat = "FBFBBFFRLR"
    result = binary_boarding1.get_col(seat) 
    assert result == 5

def test_binary_boarding1():
    file = "Day5/test_input.txt"
    result = binary_boarding1.main(file) 
    assert result == 820