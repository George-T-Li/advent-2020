import adapter_array1, adapter_array2, pytest

def test_adapter_array1_ex1():
    file = "Day10/test_input1.txt"
    result = adapter_array1.main(file)
    assert result[0] == 35

def test_adapter_array1_ex2():
    file = "Day10/test_input2.txt"
    result = adapter_array1.main(file) 
    assert result[0] == 220

def test_adapter_array2_ex1():
    file = "Day10/test_input1.txt"
    result = adapter_array2.main(file) 
    assert result == 8

def test_adapter_array2_ex2():
    file = "Day10/test_input2.txt"
    result = adapter_array2.main(file) 
    assert result == 19208