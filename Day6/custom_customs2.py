from custom_customs1 import transform

def main(file):
    input = transform(file)

    counts_list = []
    for group in input:
        answers = list(map(set, group))
        common = answers[0]
        for a in answers:
            common = common.intersection(a)
        answers_count = len(common)
        counts_list.append(answers_count)

    return sum(counts_list)


if __name__ == "__main__":
    print(main("Day6/input.txt"))