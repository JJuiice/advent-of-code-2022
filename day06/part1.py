"""Day 6 Part 1"""

#!/usr/bin/env python3

if __name__ == "__main__":
    pre_marker_char_inx = -1
    with open("input.txt", encoding="utf-8", mode="r") as f:
        cur_inx = 0
        rep_char_list = []
        signal_str = f.readline()
        while cur_inx < len(signal_str.strip()) and pre_marker_char_inx < 0:
            signal_substr = signal_str[cur_inx:cur_inx+4]
            for i, c in enumerate(signal_substr):
                if c in signal_substr[i+1:]:
                    if c not in rep_char_list:
                        rep_char_list.append(c)
                    cur_inx += i + 1
                    break

                if i == 3:
                    for i, c in enumerate(signal_substr):
                        if c not in rep_char_list:
                            pre_marker_char_inx = cur_inx+i
                            break

                        if i == len(signal_substr) - 1:
                            cur_inx += 1
        print("Pre-marker character inx is", str(pre_marker_char_inx + 1))
