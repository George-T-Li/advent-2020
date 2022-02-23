from encoding_error1 import transform, main as ee1_main

def main(file, len_preamble):
    input = transform(file)
    target = ee1_main(file, len_preamble)

    total = 0
    s, e = 0, 1
    while True:
        l = input[s:e]
        total = sum(l)
        if total < target:
            e += 1
        elif total > target:
            s += 1
            e = s + 1
        else: #total == target
            break
        
        if input[e] == target:
            return "Set not found!"
    
    return min(l) + max(l)


if __name__ == "__main__":
    print(main("Day9/input.txt", 25))