from math import lcm

def main(buses):
    ids_table = {}
    ids = []
    for index, id in enumerate(buses):
        if id != "x":
            ids_table[int(id)] = index
            ids.append(int(id))

    current_time = ids[0]
    ids_so_far = [ids[0]]
    for index, id in enumerate(ids[1:]):
        next = lcm(*ids_so_far)
        while (current_time + ids_table[id]) % id != 0:
            current_time += next
        ids_so_far.append(id)
        
    return current_time

def transform(file):
    with open(file) as f:
        input = f.readlines()
    input = list(map(lambda x: x.strip(), input))
    buses = input[1].split(",")
    return buses

if __name__ == "__main__":
    buses = transform("Day13/input.txt")
    print(main(buses))