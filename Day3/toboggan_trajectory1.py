def main():
    with open("Day3\input.txt") as f:
        input = f.readlines()
    input = list(map(lambda x: x.strip(), input))
    width = len(input[0])

    r = 3
    position = 0
    tree_count = 0
    for row in input:
        if row[position] == "#":
            tree_count += 1
        position = (position + 3) % width

    print(tree_count)


if __name__ == "__main__":
    main()