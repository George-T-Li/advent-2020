def main(file):
    with open(file) as f:
        input = f.readlines()
    input = list(map(int, input))
    input.sort()
    
    for value in input:
        new_l = input.copy()
        new_l.remove(value)
        start, end = 0, len(new_l) - 1
        sum = value + new_l[start] + new_l[end]
        while sum != 2020:
            if sum > 2020:
                end -= 1
            else:
                start += 1
            if start == end: break
            sum = value + new_l[start] + new_l[end]
            if sum == 2020:
                return value * new_l[start] * new_l[end]
    

if __name__ == "__main__":
    print(main("Day1/input.txt"))
