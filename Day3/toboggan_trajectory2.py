def main(file):
    with open(file) as f:
        input = f.readlines()
    input = list(map(lambda x: x.strip(), input))
    width = len(input[0])
    trials = [{"r": 1, "d": 1}, {"r": 3, "d": 1}, {"r": 5, "d": 1}, {"r": 7, "d": 1}, {"r": 1, "d": 2}, ]
    tree_counts = []
    
    for trial in trials:
        right = trial["r"]
        down = trial["d"]
        row = 0
        position = 0
        tree_count = 0
        while row < len(input):
            cur_row = input[row]
            if cur_row[position] == "#":
                tree_count += 1
            position = (position + right) % width
            row += down

        tree_counts.append(tree_count)

    product = 1
    for value in tree_counts:
        product *= value

    return product

if __name__ == "__main__":
    print(main("Day3/input.txt"))