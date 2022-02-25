import rain_risk1, rain_risk2, pytest

def test_rain_risk1():
    file = "Day12/test_input.txt"
    result = rain_risk1.main(file) 
    assert result == 25

def test_rain_risk2():
    file = "Day12/test_input.txt"
    result = rain_risk2.main(file) 
    assert result == 286