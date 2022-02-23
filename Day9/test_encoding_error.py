import encoding_error1, encoding_error2, pytest

def test_encoding_error1():
    file = "Day9/test_input.txt"
    result = encoding_error1.main(file, 5) 
    assert result == 127

def test_encoding_error2():
    file = "Day9/test_input.txt"
    result = encoding_error2.main(file, 5) 
    assert result == 62