"""Day 1 Part 2"""

#!/usr/bin/env python3

if __name__ == "__main__":
    top_3_cal_elves = [(0, 0)]*3
    with open("input.txt", encoding="utf-8") as f:
        cur_elf_val_n_inx = (0, 0)
        for line in f:
            if len(line.strip()) == 0:
                if cur_elf_val_n_inx[1] < 3:
                    top_3_cal_elves[cur_elf_val_n_inx[1]] = (
                        cur_elf_val_n_inx[0], cur_elf_val_n_inx[1])
                else:
                    lowest_cal_val_n_inx = (top_3_cal_elves[0][0], 0)
                    for i, number in enumerate(top_3_cal_elves):
                        if lowest_cal_val_n_inx[0] > number[0]:
                            lowest_cal_val_n_inx = (number[0], i)

                    if cur_elf_val_n_inx[0] > lowest_cal_val_n_inx[0]:
                        top_3_cal_elves[lowest_cal_val_n_inx[1]
                                        ] = cur_elf_val_n_inx

                cur_elf_val_n_inx = (0, cur_elf_val_n_inx[1] + 1)
            else:
                cur_elf_val_n_inx = (
                    cur_elf_val_n_inx[0] + int(line.strip()), cur_elf_val_n_inx[1])
    print("Elves ", str(top_3_cal_elves[0][1]), ", ", str(top_3_cal_elves[1][1]), ", and ", str(
        top_3_cal_elves[2][1]), " have the most Calories for a total ",
        str(top_3_cal_elves[0][0] + top_3_cal_elves[1][0] + top_3_cal_elves[2][0]), sep="")
