with open("file.csv", "r") as file:
    file = file.read().splitlines()

for row in file:
    row_data = row.split(",")
    print("{0} is {1} years old and {2}.".format(row_data[0],row_data[1],row_data[2]))