from time import sleep

def main(file):
    input = transform(file)
    h_size = len(input[0])
    v_size = len(input)

    def occ_neighbours(grid, x, y):
        n = 0
        n_y = y
        while not n:
            if n_y-1 >= 0:
                n_y -= 1
                if grid[n_y][x] == "#":
                    n = 1
                elif grid[n_y][x] == "L":
                    break
            else:
                break

        ne = 0
        ne_x, ne_y = x, y
        while not ne:
            if ne_x+1 < h_size and ne_y-1 >= 0:
                ne_x += 1
                ne_y -= 1
                if grid[ne_y][ne_x] == "#":
                    ne = 1
                elif grid[ne_y][ne_x] == "L":
                    break
            else:
                break

        e = 0
        e_x = x
        while not e:
            if e_x+1 < h_size:
                e_x += 1
                if grid[y][e_x] == "#":
                    e = 1
                elif grid[y][e_x] == "L":
                    break
            else:
                break

        se = 0
        se_x, se_y = x, y
        while not se:
            if se_x+1 < h_size and se_y+1 < v_size:
                se_x += 1
                se_y += 1
                if grid[se_y][se_x] == "#":
                    se = 1
                elif grid[se_y][se_x] == "L":
                    break
            else:
                break

        s = 0
        s_y = y
        while not s:
            if s_y+1 < v_size:
                s_y += 1
                if grid[s_y][x] == "#":
                    s = 1
                elif grid[s_y][x] == "L":
                    break
            else:
                break

        sw = 0
        sw_x, sw_y = x, y
        while not sw:
            if sw_x-1 >= 0 and sw_y+1 < v_size:
                sw_x -= 1
                sw_y += 1
                if grid[sw_y][sw_x] == "#":
                    sw = 1
                elif grid[sw_y][sw_x] == "L":
                    break
            else:
                break

        w = 0
        w_x = x
        while not w:
            if w_x-1 >= 0:
                w_x -= 1
                if grid[y][w_x] == "#":
                    w = 1
                elif grid[y][w_x] == "L":
                    break
            else:
                break

        nw = 0
        nw_x, nw_y = x, y
        while not nw:
            if nw_x-1 >= 0 and nw_y-1 >= 0:
                nw_x -= 1
                nw_y -= 1
                if grid[nw_y][nw_x] == "#":
                    nw = 1
                elif grid[nw_y][nw_x] == "L":
                    break
            else:
                break

        return n+ne+e+se+s+sw+w+nw

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
                    if count >= 5:
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