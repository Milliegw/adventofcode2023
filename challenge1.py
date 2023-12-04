#puzzle input - hard to read values
#combine first digit and last digit to form a single two-digit number.
# add these together to produce a single number.

# 1. Read the file puzzle_1.txt
# 2. Read the first line
# 3. For each line select the first and last digit

def find_first_and_last_integer(line):
    first_integer = line[0]
    last_integer = line[-2]

    for char in line:
        if char.isdigit():
            first_integer = char
            break

    for char in reversed(line):
        if char.isdigit():
            last_integer = char
            break

    #return int(first_integer) if first_integer else None, int(last_integer) if last_integer else None
    return first_integer, last_integer

with open("puzzle_1.txt", "r") as myfile:
    data = myfile.readlines()
    print(data)
    total = 0
    for line in data:
        first_integer, last_integer = find_first_and_last_integer(line)
        result_1 = first_integer + last_integer
        print(result_1)

        total += int(result_1)
        print(total)




