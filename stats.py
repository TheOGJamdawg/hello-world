fileName = input("Enter the file name: ") # for this use numbers.txt from the chapter
f = open(fileName, 'r')

numbers = []
for line in f:
    words = line.split()
    for word in words:
        numbers.append(float(word))

if not numbers:
    print(0)
        
numbers.sort()

midpoint = len(numbers) // 2
print("The median is", end=" ")
if len(numbers) % 2 == 1:
    print(numbers[midpoint])
else:
    print((numbers[midpoint] + numbers[midpoint - 1]) / 2)

words = []
f = open(fileName, 'r')
for line in f:
    wordsInLine = line.split()
    for word in wordsInLine:
        words.append(word.upper())

theDictionary = {}
for word in words:
    number = theDictionary.get(word, None)
    if number is None:
        theDictionary[word] = 1
    else:
        theDictionary[word] = number + 1

theMaximum = max(theDictionary.values())
for key in theDictionary:
    if theDictionary[key] == theMaximum:
        print("The mode is", key)
        break

mean = sum(numbers) / len(numbers)
print("The mean is", mean)
