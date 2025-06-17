bounceIndex = 0.6
startingHeight = float(input("Enter the height (in feet) to drop the ball from: "))
bounces = int(input("Enter the number of bounces: "))
count = 0
currentDistance = 0
totalDistance = 0
currentHeight = startingHeight
while count < bounces:
    currentDistance = currentHeight + (currentHeight * bounceIndex)
    totalDistance = totalDistance + currentDistance
    currentHeight = currentHeight * bounceIndex
    count += 1
print("The ball travelled", totalDistance, "feet with", bounces, "bounces!")

