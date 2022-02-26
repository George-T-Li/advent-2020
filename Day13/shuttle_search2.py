def main(buses):
    first = int(buses[0])

    while True:
        #if first > 100000000000000:
        for index, bus in enumerate(buses):
            if bus != 'x':
                if (first + index) % int(bus) != 0:
                    break
        else:
            return first
        first += int(buses[0])


def transform(file):
    with open(file) as f:
        input = f.readlines()
    input = list(map(lambda x: x.strip(), input))
    buses = input[1].split(",")
    return buses

if __name__ == "__main__":
    buses = transform("Day13/input.txt")
    print(main(buses))