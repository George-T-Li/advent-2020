def main(file):
    input = transform(file)
    
    accumulator = 0
    line = 0

    seen_lines = set()
    while True:
        if line in seen_lines:
            break
        else:
            seen_lines.add(line)

        operation = input[line][0]
        arg = input[line][1]
        sign, n = arg[0], int(arg[1:])
        if operation == "acc":
            if sign == "+":
                accumulator += n
            else:
                accumulator -= n
            line += 1
        elif operation == "jmp":
            if sign == "+":
                line += n
            else:
                line -= n
        elif operation == "nop":
            line += 1
    
    return accumulator
    

def transform(file):
    with open(file) as f:
        input = f.readlines()
    input = list(map(lambda x: x.split(), input))
    return input

if __name__ == "__main__":
    print(main("Day8/input.txt"))