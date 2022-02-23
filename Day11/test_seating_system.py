import seating_system1, seating_system2, pytest

def test_seating_system1():
    file = "Day11/test_input.txt"
    result = seating_system1.main(file) 
    assert result == 37

def test_seating_system2():
    file = "Day11/test_input.txt"
    result = seating_system2.main(file) 
    assert result == 26