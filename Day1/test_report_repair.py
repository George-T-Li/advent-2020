import report_repair1, report_repair2, pytest

def test_report_repair1():
    file = "Day1/test_input.txt"
    result = report_repair1.main(file) 
    assert result == 514579

def test_report_repair2():
    file = "Day1/test_input.txt"
    result = report_repair2.main(file)
    assert result == 241861950