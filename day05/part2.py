"""Day 5 Part 2"""

#!/usr/bin/env python3

if __name__ == "__main__":
    # Yes I hardcoded this. Do I wish I did a parser instead?
    # A little bit, yes.
    #
    # Is the joy of completing the challenge at 12 AM before work the next day enough to overcome that regret?
    # Abso-freakin-lutely.
    crate_stacks = [
        ["Q", "M", "G", "C", "L"],
        ["R", "D", "L", "C", "T", "F", "H", "G"],
        ["V", "J", "F", "N", "M", "T", "W", "R"],
        ["J", "F", "D", "V", "Q", "P"],
        ["N", "F", "M", "S", "L", "B", "T"],
        ["R", "N", "V", "H", "C", "D", "P"],
        ["H", "C", "T"],
        ["G", "S", "J", "V", "Z", "N", "H", "P"],
        ["Z", "F", "H", "G"]
    ]
    with open("moves.txt", encoding="utf-8", mode="r") as f:
        for line in f:
            asd = [int(c) for c in line if c.isdigit()]
            if len(asd) > 3:
                asd[0] = int(str(asd[0]) + str(asd[1]))
                asd.pop(1)
            for i in range(asd[0]):
                crate_stacks[asd[2] - 1].append(crate_stacks[asd[1] - 1].pop(-(asd[0] - i)))
        print("Top of each stack values: ", end="")
        for stack in crate_stacks:
            print(stack[-1], end="")
        print("")
