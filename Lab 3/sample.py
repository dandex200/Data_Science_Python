import sys
import os
import random

# Check to see if sufficient number of arguments
if len(sys.argv) != 3:
    print("WARNING: Insufficient number of command line arguments")
    sys.exit()

# Check to see if file exists
file_path = sys.argv[1]
if os.path.isfile(file_path) == 0:
    print("WARNING: File entered does not exist")
    sys.exit()

# Identify number of random lines
random_num_total = int(sys.argv[2])

# Read in lines
f_in = open(sys.argv[1], "r")
lines = []
for l in f_in.readlines():
    lines.append(l.strip())
f_in.close()

# Shuffle lines list
random.shuffle(lines)

# Create list that is length of num entered from the random list
count = 0
random_lines = []
for p in lines:
    if count == random_num_total:
        break
    count += 1
    random_lines.append(p)

# Print random Lines
print("Random lines: %s \n" % random_lines)
