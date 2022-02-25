def main(file):
    input = transform(file)
    
    loc = (0, 0)
    facing = "E"
    ang_dir = {"E": 0, "S": 90, "W": 180, "N": 270}
    dir_ang = {0: "E", 90: "S", 180: "W", 270: "N"}


    for inst in input:
        action = inst[0]
        value = int(inst[1:])
        angle = ang_dir[facing]
        if action == "L":
            angle = (angle - value) % 360
            facing = dir_ang[angle]
        elif action == "R":
            angle = (angle + value) % 360
            facing = dir_ang[angle]
        elif action == "F":
            if facing == "E":
                loc = (loc[0] + value, loc[1])
            elif facing == "S":
                loc = (loc[0], loc[1] + value)
            elif facing == "W":
                loc = (loc[0] - value, loc[1])
            elif facing == "N":
                loc = (loc[0], loc[1] - value)
        elif action == "E":
            loc = (loc[0] + value, loc[1])
        elif action == "S":
            loc = (loc[0], loc[1] + value)
        elif action == "W":
            loc = (loc[0] - value, loc[1])
        elif action == "N":
            loc = (loc[0], loc[1] - value)

    return abs(loc[0]) + abs(loc[1])

def transform(file):
    with open(file) as f:
        input = f.readlines()
    input = list(map(lambda x: x.strip(), input))
    return input

if __name__ == "__main__":
    print(main("Day12/input.txt"))