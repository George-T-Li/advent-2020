from handheld_halting1 import transform

def main(file):
    input = transform(file)

    jmp_lines = []
    nop_lines = []
    for index, instruction in enumerate(input):
        operation = instruction[0]
        arg = instruction[1]
        if operation == "jmp":
            jmp_lines.append([index, arg])
        elif operation == "nop":
            nop_lines.append([index, arg])
    
    for inst in jmp_lines:
        new_input = input.copy()
        new_input[inst[0]] = ["nop", inst[1]]
        result = no_loop(new_input)
        if result:
            return result
    
    for inst in nop_lines:
        new_input = input.copy()
        new_input[inst[0]] = ["jmp", inst[1]]
        result = no_loop(new_input)
        if result:
            return result

    return "They all have inf loops!"

def no_loop(input):    
    accumulator = 0
    line = 0

    seen_lines = set()
    while True:
        if line == len(input):
            return accumulator
        elif line in seen_lines:
            return False
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

if __name__ == "__main__":
    print(main("Day8/input.txt"))