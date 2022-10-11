import sys

# Confirm sufficient number of arguments
if len(sys.argv) != 3:
    print("Must specificy two files to be compared.")
    sys.exit()

#  Read numbers, strip and convert into integers from files


def read_num(input_path):
    numbers = set()
    f_in = open(input_path, "r")
    for l in f_in.readlines():
        l = l.strip()
        num = int(l)
        numbers.add(num)
    f_in.close()
    return numbers


# Read input Files
numbers1 = read_num(sys.argv[1])
numbers2 = read_num(sys.argv[2])

# Create Strings of file names from input arguments
file_1 = str(sys.argv[1])
file_2 = str(sys.argv[2])
# Find Overlap between two files
overlap = numbers1.intersection(numbers2)

# Print filenames and overlap
print("Overlap between %s and %s is: \n %s" % (file_1, file_2, overlap))
