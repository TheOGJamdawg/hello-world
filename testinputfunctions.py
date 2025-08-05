"""
File: testinputfunctions.py

Defines a function for robust input of ints.
"""

def inputInt(prompt):
    """Guarantees that the user inputs an integer,
    using the given prompt. Returns the integer."""
    while True:
        theString = input(prompt)
        if theString.isdigit():
            return int(theString)
        else:
            print("Error: the input must consist only of digits")

def inputFloat(prompt):
    """Float input. Check for digits and maximum 1 decimal point"""
    while True:
        theInput = input(prompt)
        decimalCount = 0 # initialize counter
        valid = True

        for char in theInput:
            if char.isdigit():
                continue
            elif char == '.':
                decimalCount += 1 # count how many decimals are entered
            else:
                valid = False # error if more than 1 decimal

        if valid and decimalCount <= 1: 
            return float(theInput)
        else:
            print("Error: the input must consist only of digits and maximum 1 decimal point")

def main():
    n = inputInt("Please enter an integer: ")
    print(f"Integer entered: {n}")
    
    f = inputFloat("Please enter a floating-point number: ")
    print(f"Float entered: {f}")

if __name__ == "__main__":
    main()
