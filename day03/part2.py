"""Day 3 Part 2"""

#usr/bin/env python3

if __name__ == "__main__":
    total_priority = 0
    with open("input.txt", encoding="utf-8") as f:
        elf_group_sacks = [""]*3
        for count, line in enumerate(f):
            elf_group_sacks[count % 3] = line
            if count % 3 == 2:
                matching_letter = ""
                for l in elf_group_sacks[0]:
                    if l in elf_group_sacks[1] and l in elf_group_sacks[2]:
                        matching_letter = l
                        break
                if matching_letter.isupper():
                    total_priority += ord(matching_letter) - 38
                else:
                    total_priority += ord(matching_letter) - 96
    print("The total priority is", str(total_priority))
