import handy_haversacks1, handy_haversacks2, pytest

def test_handy_haversacks1():
    file = "Day7/test_input1.txt"
    result = handy_haversacks1.main(file) 
    assert result == 4

def test_handy_haversacks2_ex1():
    file = "Day7/test_input1.txt"
    result = handy_haversacks2.main(file) 
    assert result == 32

def test_handy_haversacks2_ex2():
    file = "Day7/test_input2.txt"
    result = handy_haversacks2.main(file) 
    assert result == 126