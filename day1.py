import sys

def getRepeatedFreq():
    current_freq = 0
    freq_list = []
    repeat_found = False
    while not repeat_found:
        with open("sourceFiles/day1input.txt") as f:
            for line in f:
                current_freq += int(line)
                if current_freq in freq_list:
                    repeat_found = True
                    break
                else:
                    print("Adding {} to list".format(current_freq))
                    freq_list.append(current_freq)
    return current_freq

with open("sourceFiles/day1input.txt") as f:

    freq = 0
    for line in f:
        freq += int(line)
    
print("Final Frequency: {}".format(freq))


print("First Repeated Frequency: {}".format(getRepeatedFreq()))
    