def main(file):
    bags = transform(file)

    search_for = {"shiny gold"}
    valid_bags = set()

    while search_for:
        temp = set()
        for b in search_for:
            for bag, contents in bags.items():
                if b in contents:
                    temp.add(bag)
                    valid_bags.add(bag)
        search_for = temp.copy()
                 
    return len(valid_bags)

def transform(file):
    with open(file) as f:
        input = f.readlines()
    bags = {}
    for rule in input:
        i1 = rule.index(" bags")
        i2 = rule.index("contain ") + 7
        bags[rule[:i1]] = rule[i2:].strip("\n")
    return bags

if __name__ == "__main__":
    print(main("Day7/input.txt"))