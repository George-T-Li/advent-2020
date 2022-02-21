def main(file):
    bags = transform(file)

    curr_bag = "shiny gold"
    count = bag_count(bags, curr_bag)

    return count

def bag_count(bags, curr_bag):
    contents = bags[curr_bag]
    if contents is None:
        return 0

    count = 0
    for bag, n in contents.items():
        count += int(n) 
        count += int(n) * bag_count(bags, bag)
    return count

def transform(file):
    with open(file) as f:
        input = f.readlines()

    bags = {}
    for rule in input:
        i1 = rule.index(" bags")
        i2 = rule.index("contain ") + 7
        temp = rule[i2:].strip()
        temp = temp.replace("bags", "bag")
        temp = temp.replace(".", ",")
        if temp == "no other bag,":
            bags[rule[:i1].strip()] = None
        else:
            contents = list(map(lambda x: x.strip(), temp.split("bag,")))
            d = {}
            for value in contents[:-1]:
                d[value[2:]] = value[0]
            bags[rule[:i1].strip()] = d

    return bags

if __name__ == "__main__":
    print(main("Day7/input.txt"))