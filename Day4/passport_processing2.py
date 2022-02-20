from pkg_resources import parse_requirements
from passport_processing1 import transform, missing_cid

def main(file):
    passports = transform(file)

    valid_passport_count = 0
    for passport in passports:
        if len(passport) == 8 and validate(passport):
            valid_passport_count += 1
        elif len(passport) == 7 and missing_cid(passport) and validate(passport):
            valid_passport_count += 1

    return valid_passport_count

def validate(passport):
    if int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
        return False
    if int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
        return False
    if int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030:
        return False

    if passport["hgt"][-2:] not in ["cm", "in"]:
        return False
    else:
        height = int(passport["hgt"][:-2])
        if "cm" in passport["hgt"]:
            if height < 150 or height > 193:
                return False
        elif "in" in passport["hgt"]:
            if height < 59 or height > 76:
                return False

    hcl = passport["hcl"]
    if len(hcl) != 7:
        return False
    else:
        if hcl[0] != "#":
            return False
        else:
            h = "0123456789abcdef"
            if (hcl[1] not in h) or (hcl[2] not in h) or (hcl[3] not in h) or (hcl[4] not in h) or (hcl[5] not in h) or (hcl[6] not in h):
                return False
    
    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    
    pid = passport["pid"]
    if len(pid) != 9:
        return False
    else:
        n = "0123456789"
        if (pid[0] not in n) or (pid[1] not in n) or (pid[2] not in n) or (pid[3] not in n) or \
            (pid[4] not in n) or (pid[5] not in n) or (pid[6] not in n) or (pid[7] not in n) or (pid[8] not in n):
            return False
    
    return True

if __name__ == "__main__":
    print(main("Day4/input.txt"))
