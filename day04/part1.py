"""Day 4 Part 1"""

#!/usr/bin/env python3

if __name__ == "__main__":
    tfoap = 0
    with open("input.txt", encoding="utf-8", mode="r") as f:
        for line in f:
            str_range_1 = line.strip().split(',')[0].split('-')
            str_range_2 = line.strip().split(',')[1].split('-')
            if ((int(str_range_1[0]) <= int(str_range_2[0])
                and int(str_range_1[1]) >= int(str_range_2[1]))
                or (int(str_range_2[0]) <= int(str_range_1[0])
                and int(str_range_2[1]) >= int(str_range_1[1]))):
                tfoap += 1
    print ("Total number of overlaps:", str(tfoap))
