def main(file):
    input = transform(file)

    seat_ids = []
    for seat in input:
        row = get_row(seat)
        col = get_col(seat)
        id = row * 8 + col
        seat_ids.append(id)

    return max(seat_ids)


def transform(file):
    with open(file) as f:
        input = f.readlines()
    input = list(map(lambda x: x.strip(), input))
    return input

def get_row(seat):
    seat_rows = seat[:7]
    l, u = 0, 127
    for index, half in enumerate(seat_rows):
        power = 6 - index
        if half == "F":
            u -= 2**power
        else:
            l += 2**power
    return u

def get_col(seat):
    seat_cols = seat[7:]
    l, u = 0, 7
    for index, half in enumerate(seat_cols):
        power = 2 - index
        if half == "L":
            u -= 2**power
        else:
            l += 2**power
    return u


if __name__ == "__main__":
    print(main("Day5/input.txt"))