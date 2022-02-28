from docking_data1 import prepend_zeros, transform
from itertools import product

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
            value = int(l[1])
            addresses = address_bitmask(mask, address)
            for a in addresses:
                mem[a] = value

    return sum(mem.values())

def address_bitmask(mask, address):
    address = prepend_zeros(bin(address), 36)[2:]

    mask_segments = mask.split("X")
    address_segments = []
    index = 0
    for m_s in mask_segments:
        if len(m_s) == 0:
            a_s = ""
        else:
            a_s = address[index:index+len(m_s)]
            a_s = prepend_zeros("0b" + bitwise_or(m_s, a_s), len(m_s))[2:]
            index += (len(m_s)+1)
        address_segments.append(a_s)
    count_X = len(address_segments) - 1

    possibilities = product("01", repeat=count_X)
    addresses = []
    for p in possibilities:
        a = ""
        for index, segment in enumerate(address_segments[:-1]):
            a = a + segment + p[index]
        a = int(a + address_segments[-1], 2)
        addresses.append(a)

    return addresses

def bitwise_or(a, b):
    result = int(a, 2) | int(b, 2)
    return bin(result)[2:]

if __name__ == "__main__":
    print(main("Day14/input.txt"))