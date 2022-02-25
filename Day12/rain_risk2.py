from rain_risk1 import transform

def main(file):
    input = transform(file)

    loc = (0, 0)
    wp_rel_loc = (10, 1)
    ang_dir = {"E": 0, "S": 90, "W": 180, "N": 270}
    dir_ang = {0: "E", 90: "S", 180: "W", 270: "N"}

    for inst in input:
        action = inst[0]
        value = int(inst[1:])
        if action == "L":
            if value == 90:
                wp_rel_loc = (-wp_rel_loc[1], wp_rel_loc[0])
            elif value == 180:
                wp_rel_loc = (-wp_rel_loc[0], -wp_rel_loc[1])
            elif value == 270:
                wp_rel_loc = (wp_rel_loc[1], -wp_rel_loc[0])
        elif action == "R":
            if value == 90:
                wp_rel_loc = (wp_rel_loc[1], -wp_rel_loc[0])
            elif value == 180:
                wp_rel_loc = (-wp_rel_loc[0], -wp_rel_loc[1])
            elif value == 270:
                wp_rel_loc = (-wp_rel_loc[1], wp_rel_loc[0])
        elif action == "F":
            for _ in range(value):
                loc = (loc[0] + wp_rel_loc[0], loc[1] + wp_rel_loc[1])
        elif action == "E":
            wp_rel_loc = (wp_rel_loc[0] + value, wp_rel_loc[1])
        elif action == "S":
            wp_rel_loc = (wp_rel_loc[0], wp_rel_loc[1] - value)
        elif action == "W":
            wp_rel_loc = (wp_rel_loc[0] - value, wp_rel_loc[1])
        elif action == "N":
            wp_rel_loc = (wp_rel_loc[0], wp_rel_loc[1] + value)

    return abs(loc[0]) + abs(loc[1])


if __name__ == "__main__":
    print(main("Day12/input.txt"))