"""Day 3 Part 1"""

#usr/bin/env python3

if __name__ == "__main__":
    total_priority = 0
    with open("input.txt", encoding="utf-8") as f:
        for line in f:
            comp_1 = line[:int(len(line.strip())/2)]
            comp_2 = line[int(len(line.strip())/2):]
            matching_letter = ""
            for l in comp_1:
                if l in comp_2:
                    matching_letter = l
                    break
            if matching_letter.isupper():
                total_priority += ord(matching_letter) - 38
            else:
                total_priority += ord(matching_letter) - 96
    print("The total priority is", str(total_priority))
