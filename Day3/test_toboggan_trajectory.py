import toboggan_trajectory1, toboggan_trajectory2, pytest

def test_toboggan_trajectory1():
    file = "Day3/test_input.txt"
    result = toboggan_trajectory1.main(file) 
    assert result == 7

def test_toboggan_trajectory2():
    file = "Day3/test_input.txt"
    result = toboggan_trajectory2.main(file)
    assert result == 336