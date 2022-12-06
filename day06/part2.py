"""Day 6 Part 2"""

#!/usr/bin/env python3

if __name__ == "__main__":
    start_of_packet_inx = -1
    start_of_msg_marker = -1
    with open("input.txt", encoding="utf-8", mode="r") as f:
        cur_inx = 0
        signal_str = f.readline()
        while cur_inx < len(signal_str.strip()) and start_of_msg_marker < 0:
            if start_of_packet_inx > -1:
                signal_substr = signal_str[cur_inx:cur_inx+14]
            else:
                signal_substr = signal_str[cur_inx:cur_inx+4]

            for i, c in enumerate(signal_substr):
                if c in signal_substr[i+1:]:
                    cur_inx += i + 1
                    break

                if i == len(signal_substr) - 1:
                    if start_of_packet_inx > 0:
                        start_of_msg_marker = cur_inx+i
                    else:
                        cur_inx += i-3
                        start_of_packet_inx = cur_inx
                    break
        print("Start of message marker is after character", str(start_of_msg_marker + 1))
