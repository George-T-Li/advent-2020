def main():
    with open("Day1\input.txt") as f:
        input = f.readlines()
    input = list(map(int, input))
    input.sort()
    
    start, end = 0, len(input) - 1
    sum = input[start] + input[end]
    while sum != 2020:
        if sum > 2020:
            end -= 1
        else:
            start += 1
        sum = input[start] + input[end]
    print (input[start]*input[end])

if __name__ == "__main__":
    main()
