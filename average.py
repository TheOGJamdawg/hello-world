from functools import reduce

def main():
    filename = input("Enter the filename: ") # for this assignment I am using numbers.txt from Week 7 and including it in the zip

    with open(filename, 'r') as file:
        content = file.read()
        parts = content.split() #separate the numbers
        numbers = list(map(float, parts))

        total = reduce(lambda a, b: a + b, numbers)
        average = total / len(numbers)
        print("The average is:", round(average, 2)) #rounding to 2 digits

main()
