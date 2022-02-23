from adapter_array1 import main as aa1_main

def main(file):
    part1 = aa1_main(file)
    diff1 = part1[1]

    buckets = []
    bucket = [diff1[0]]
    curr_a = diff1[0]
    for a in diff1[1:]:
        if a == curr_a + 1:
            bucket.append(a)
            curr_a = a
        else:
            buckets.append(bucket)
            bucket = [a]
            curr_a = a
    buckets.append(bucket)

    count = 1
    for bucket in buckets:
        count *= count_arrangements(bucket)

    return count

def count_arrangements(bucket):
    size = len(bucket)
    if size == 1:
        return 1
    elif size == 2:
        return 2
    elif size == 3:
        return 4
    else:
        count = 0
        count += count_arrangements(bucket[1:])
        count += count_arrangements(bucket[2:])
        count += count_arrangements(bucket[3:])
        return count

if __name__ == "__main__":
    print(main("Day10/input.txt"))
