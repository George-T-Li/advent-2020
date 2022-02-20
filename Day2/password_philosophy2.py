def main(file):
    with open(file) as f:
        input = f.readlines()
    input = list(map(lambda x: x.split(), input))

    valid_count = 0
    for item in input:
        positions = list(map(int, item[0].split("-")))
        p = list(map(lambda x: x-1, positions)) #1-based indexing
        letter = item[1][0]
        password = item[2]
        if password[p[0]] == letter and password[p[1]] != letter:
            valid_count += 1
        elif password[p[0]] != letter and password[p[1]] == letter:
            valid_count += 1
    
    return valid_count


if __name__ == "__main__":
    print(main("Day2/input.txt"))