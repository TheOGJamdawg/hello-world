fileName = input("Enter the Filename: ") # I used numbers.txt for testing this
f = open(fileName, 'r')
lines = f.readlines()

print("The total lines in the file: ", len(lines))

while True:
    lineNumber = int(input("Enter a line number (Use '0' to quit the program: "))

    if lineNumber == 0:
        exit()

    if 1 <= lineNumber <= len(lines):
        print("Line", str(lineNumber) + ":", lines[lineNumber - 1])
    else:
        print("There are only", len(lines), "lines in the file, please use a smaller number.")
