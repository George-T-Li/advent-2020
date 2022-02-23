from time import sleep

def main(file):
    input = transform(file)
    h_size = len(input[0])
    v_size = len(input)

    def occ_neighbours(grid, x, y):
        neighbours = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]
        count = 0
        for seat in neighbours:
            if 0 <= seat[0] <= h_size-1 and 0 <= seat[1] <= v_size-1:
                if grid[seat[1]][seat[0]] == "#":
                    count += 1
        return count

    def apply_rules(grid, changed):
        updated_grid = []
        changed = False
        for y, row in enumerate(grid):
            updated_row = []
            for x, seat in enumerate(row):
                count = occ_neighbours(grid, x, y)
                if seat == "L":
                    if count == 0:
                        updated_row.append("#")
                        changed = True
                    else:
                        updated_row.append("L")
                elif seat == "#":
                    if count >= 4:
                        updated_row.append("L")
                        changed = True
                    else:
                        updated_row.append("#")
                else:
                    updated_row.append(".")
            updated_grid.append("".join(updated_row))
        return updated_grid, changed

    changed = True
    while changed:
        apply = apply_rules(input, changed)
        changed = apply[1]
        input = apply[0]

    count = 0
    for row in input:
        for seat in row:
            if seat == "#":
                count += 1

    return count

def transform(file):
    with open(file) as f:
        input = f.readlines()
    input = list(map(lambda x: x.strip(), input))
    return input


if __name__ == "__main__":
    print(main("Day11/input.txt"))