def main(file):
    input = transform(file)

    counts_list = []
    for group in input:
        answers = "".join(group)
        answers_count = 0
        for char in "abcdefghijklmnopqrstuvwxyz":
            if char in answers:
                answers_count += 1
        counts_list.append(answers_count)

    return sum(counts_list)

def transform(file):
    with open(file) as f:
        input = f.readlines()
        
    groups = []
    group = ""
    for row in input:
        if row == "\n":
            groups.append(group.replace("\n", " "))
            group = ""
        else:
            group += row
    groups.append(group.replace("\n", " "))
    return list(map(lambda x: x.split(), groups))



if __name__ == "__main__":
    print(main("Day6/input.txt"))