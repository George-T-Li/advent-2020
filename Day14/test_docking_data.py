import docking_data1, docking_data2, pytest

def test_prepend_zeros():
    b_string = '0b1011'
    result = docking_data1.prepend_zeros(b_string, 36)
    assert result == "0b000000000000000000000000000000001011"

def test_bitmask():
    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
    b_string = '0b000000000000000000000000000000001011'
    result = docking_data1.bitmask(mask, b_string)
    assert result == "0b000000000000000000000000000001001001"

def test_docking_data1():
    file = "Day14/test_input.txt"
    result = docking_data1.main(file) 
    assert result == 165

def test_docking_data2():
    file = "Day14/test_input2.txt"
    result = docking_data2.main(file) 
    assert result == 208