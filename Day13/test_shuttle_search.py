import shuttle_search1, pytest

def test_shuttle_search1():
    file = "Day13/test_input.txt"
    result = shuttle_search1.main(file) 
    assert result == 295

