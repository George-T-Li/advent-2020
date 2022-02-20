import passport_processing1, passport_processing2, pytest

def test_input_transformer():
    file = "Day4/test_input.txt"
    result = passport_processing1.transform(file)
    print(result)
    assert len(result) == 4

def test_missing_cid():
    passport = {'ecl': 'amb', 'pid': '021066381', 'hcl': '#ceb3a1', 'byr': '1982', 'iyr': '2017', 'hgt': '167cm', 'eyr': '2025'}
    result = passport_processing1.missing_cid(passport)
    assert result == True

def test_not_missing_cid():
    passport = {'ecl': 'amb', 'pid': '021066381', 'hcl': '#ceb3a1', 'byr': '1982', 'iyr': '2017', 'hgt': '167cm', 'eyr': '2025', 'cid': '61'}
    result = passport_processing1.missing_cid(passport)
    assert result == False

def test_script1():
    file = "Day4/test_input.txt"
    result = passport_processing1.main(file) 
    assert result == 2

def test_valid_passport():
    passport = {'iyr': '2010', 'hgt': '158cm', 'hcl': '#b6652a', 'ecl': 'blu', 'byr': '1944', 'eyr': '2021', 'pid': '093154719'}
    result = passport_processing2.validate(passport)
    assert result == True

def test_invalid_passport():
    passport = {'eyr': '1972', 'cid': '100', 'hcl': '#18171d', 'ecl': 'amb', 'hgt': '170', 'pid': '186cm', 'iyr': '2018', 'byr': '1926'}
    result = passport_processing2.validate(passport)
    assert result == False