import sys
import os

# First we must check if there's at least 3 arguments
if len(sys.argv) < 3:
    print("Must specifiy at least one line to be printed")
    sys.exit()

# Check if File Path exists
file_path = sys.argv[1]
if os.path.isfile(file_path) == 0:
    print("file name does not exist")
    sys.exit()

# Now we need to determine what line numbers need to be printed
# Stars at second argument (first integer) and records remaining numbers as ints in line_numbers set
line_numbers = []
for s in sys.argv[2:]:
    if s.isnumeric():  # Check to see if argument is an actual integer
        num = int(s)
        line_numbers.append(num)

f_in = open(sys.argv[1], "r")
current_line_number = 0
names = []
for l in f_in.readlines():
    current_line_number += 1
    if current_line_number in line_numbers:
        names.append(l.strip())
f_in.close()
print("The names are: \n %s" % names)
