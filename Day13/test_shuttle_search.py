import shuttle_search1, pytest

def test_shuttle_search1():
    file = "Day13/test_input.txt"
    result = shuttle_search1.main(file) 
    assert result == 295

def test_shuttle_search2_ex1():
    buses = [17,"x",13,19]
    result = shuttle_search2.main(buses) 
    assert result == 3417

def test_shuttle_search2_ex2():
    buses = [67,7,59,61]
    result = shuttle_search2.main(buses) 
    assert result == 754018

def test_shuttle_search2_ex3():
    buses = [67,"x",7,59,61]
    result = shuttle_search2.main(buses) 
    assert result == 779210

def test_shuttle_search2_ex4():
    buses = [67,7,"x",59,61]
    result = shuttle_search2.main(buses) 
    assert result == 1261476

def test_shuttle_search2_ex5():
    buses = [1789,37,47,1889]
    result = shuttle_search2.main(buses) 
    assert result == 1202161486