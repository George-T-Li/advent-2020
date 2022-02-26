def main(file):
    timestamp, buses = transform(file)
    buses.sort()
    for ts in range(timestamp, timestamp + buses[-1]):
        for id in buses:
            if ts % id == 0:
                return (ts - timestamp) * id
    return "never!"

def transform(file):
    with open(file) as f:
        input = f.readlines()
    input = list(map(lambda x: x.strip(), input))
    timestamp = int(input[0])

    def not_x(id):
        return not id == 'x'
    buses = list(map(int, filter(not_x, input[1].split(","))))

    return timestamp, buses

if __name__ == "__main__":
    print(main("Day13/input.txt"))