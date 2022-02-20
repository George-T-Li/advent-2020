def main(file):
    with open(file) as f:
        input = f.readlines()
    input = list(map(lambda x: x.split(), input))

    valid_count = 0
    for item in input:
        hilo = list(map(int, item[0].split("-")))
        letter = item[1][0]
        password = item[2]
        occurrences = password.count(letter)
        if hilo[0] <= occurrences <= hilo[1]:
            valid_count += 1
    
    return valid_count


if __name__ == "__main__":
    print(main("Day2/input.txt"))