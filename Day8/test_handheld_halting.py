import handheld_halting1, pytest

def test_handheld_halting1():
    file = "Day8/test_input.txt"
    result = handheld_halting1.main(file) 
    assert result == 5