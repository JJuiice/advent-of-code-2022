#!/usr/bin/env python3

if __name__ == "__main__":
    most_cal_elf_inx = 0
    most_cal_elf_val = 0
    with open("input.txt") as f:
        cur_elf_cal_cnt = 0
        cur_elf_inx = 0
        for line in f:
            if len(line.strip()) == 0:
                if cur_elf_cal_cnt > most_cal_elf_val:
                    most_cal_elf_val = cur_elf_cal_cnt
                    most_cal_elf_inx = cur_elf_inx
                cur_elf_inx += 1
                cur_elf_cal_cnt = 0
                pass
            else:
                cur_elf_cal_cnt += int(line.strip())
    print("Elf #", str(most_cal_elf_inx + 1), " has the most Calories at a value of ", str(most_cal_elf_val), sep="")
