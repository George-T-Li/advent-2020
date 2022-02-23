def main(file):
    input = transform(file)

    input.sort()
    built_in_adapter = input[-1] + 3
    input.append(built_in_adapter)

    diff1 = []
    diff3 = []
    
    prev_jolt = 0
    for i, jolt in enumerate(input):
        diff = jolt - prev_jolt
        if diff == 1:
            diff1.append(jolt)
        elif diff == 3:
            diff3.append(jolt)
        prev_jolt = jolt

    return len(diff1) * len(diff3), diff1, diff3

def transform(file):
    with open(file) as f:
        input = f.readlines()
    input = list(map(int, input))
    return input

if __name__ == "__main__":
    print(main("Day10/input.txt"))