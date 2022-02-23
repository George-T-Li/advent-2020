def main(file, len_preamble):
    input = transform(file)

    s, e = 0, len_preamble
    prev_nums = input[s:e]
    target = input[e]
    while is_valid(prev_nums, target):
        s += 1
        e += 1
        prev_nums = input[s:e]
        target = input[e]

    return target


def is_valid(prev_nums, target):
    prev_nums.sort()
    
    start, end = 0, len(prev_nums) - 1
    sum = prev_nums[start] + prev_nums[end]
    while sum != target:
        if start == end:
            return False
        if sum > target:
            end -= 1
        else:
            start += 1
        sum = prev_nums[start] + prev_nums[end]
        
    return prev_nums[start]*prev_nums[end]

def transform(file):
    with open(file) as f:
        input = f.readlines()
    input = list(map(int, input))
    return input

if __name__ == "__main__":
    print(main("Day9/input.txt", 25))
