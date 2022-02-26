def main(file):
    input = transform(file)
    
    mask = ""
    mem = {}
    for line in input:
        if line[:4] == "mask":
            mask = line[7:]
        else:
            l = list(map(lambda x: x.strip(), line[3:].split("=")))
            address = int(l[0][1:-1])
            value = prepend_zeros(bin(int(l[1])), 36)
            value = int(bitmask(mask, value), 2)
            mem[address] = value

    return sum(list(mem.values()))

def prepend_zeros(b_string, l):
    b_num = b_string[2:]
    num_zeros = l - len(b_num)
    b_num = ("0" * num_zeros) + b_num
    return "0b" + b_num

def bitmask(mask, b_string):
    b_string = list(b_string[2:])
    for index, value in enumerate(mask):
        if value != "X":
            b_string[index] = value
    return "0b" + "".join(b_string)

def transform(file):
    with open(file) as f:
        input = f.readlines()
    input = list(map(lambda x: x.strip(), input))
    return input

if __name__ == "__main__":
    print(main("Day14/input.txt"))