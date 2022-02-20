import toboggan_trajectory1, toboggan_trajectory2, pytest

def test_report_repair1():
    file = "Day3/test_input.txt"
    result = toboggan_trajectory1.main(file) 
    assert result == 7

def test_report_repair2():
    file = "Day3/test_input.txt"
    result = toboggan_trajectory2.main(file)
    assert result == 336