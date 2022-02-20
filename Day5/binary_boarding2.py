from binary_boarding1 import transform, get_col, get_row

def main(file):
    input = transform(file)

    seat_ids = []
    for seat in input:
        row = get_row(seat)
        col = get_col(seat)
        id = row * 8 + col
        seat_ids.append(id)
    seat_ids.sort()

    for id in range(1, 837):
        if id not in seat_ids:
            if id-1 in seat_ids and id+1 in seat_ids:
                return id
    
    return "id not found"


if __name__ == "__main__":
    print(main("Day5/input.txt"))