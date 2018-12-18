import sys
import collections

with open("sourceFiles/day2input.txt") as f:
    total_2 = 0
    total_3 = 0
    for line in f:
        line = line.strip('\n')
        line_count = collections.Counter(line)
        line_has_2 = False # if the line has a character repeated exactly 2 times
        line_has_3 = False # if the line has a character repeated exactly 3 times
        total_2 += int(2 in line_count.values())
        total_3 += int(3 in line_count.values())

print("Number of characters repeated 2 times: {}".format(total_2))
print("Number of characters repeated 3 times: {}".format(total_3))
print("Checksum: {}".format(total_2*total_3))