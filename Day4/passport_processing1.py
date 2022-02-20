def main(file):
    passports = transform(file)
    print(passports)

    valid_passport_count = 0
    for passport in passports:
        if len(passport) == 8:
            valid_passport_count += 1
        elif len(passport) == 7 and missing_cid(passport):
            valid_passport_count += 1

    return valid_passport_count

def transform(file):
    with open(file) as f:
        input = f.readlines()

    temp = []
    passport = ""
    for row in input:
        if row == "\n":
            temp.append(passport.replace("\n", " "))
            passport = ""
        else:
            passport += row
    temp.append(passport.replace("\n", " "))
    temp = list(map(lambda x: x.split(), temp))

    passports = []
    for passport in temp:
        d = {}
        for field in passport:
            i = field.find(":")
            d[field[:i]] = field[i+1:]
        passports.append(d)

    return passports


def missing_cid(passport):
    return "cid" not in passport.keys()
    

if __name__ == "__main__":
    print(main("Day4/input.txt"))
