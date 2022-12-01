#!/usr/bin/env python3

if __name__ == "__main__":
    top_3_cal_elves = [(0,0)]*3
    with open("input.txt") as f:
        cur_elf_val_n_inx = (0,0)
        for line in f:
            if len(line.strip()) == 0:
                top_3_cal_elves = [cur_elf_val_n_inx if cur_elf_val_n_inx[0] > x[0] else x for x in top_3_cal_elves]
                cur_elf_val_n_inx = (0, cur_elf_val_n_inx[1] + 1)
                pass
            else:
                cur_elf_val_n_inx = (cur_elf_val_n_inx[0] + int(line.strip()), cur_elf_val_n_inx[1])
    print("Elves ", str(top_3_cal_elves[0][1]), ", ", str(top_3_cal_elves[1][1]), ", and ", str(top_3_cal_elves[2][1]), " have the most Calories for a total ", str(top_3_cal_elves[0][0] + top_3_cal_elves[1][0] + top_3_cal_elves[2][0]), sep="")
