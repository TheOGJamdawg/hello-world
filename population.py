initialNumber = int(input("Enter the intial number of organisms: "))
growthRate = float(input("Enter growth rate: "))
growthHours = int(input("Enter number of hours it takes to achieve growth rate: "))
totalHours = int(input("Enter the total number of hours the organisms are allowed to grow: "))
rounds = totalHours / growthHours
population = initialNumber * growthRate
totalPopulation = initialNumber * growthRate ** rounds
print("Organisms after", growthHours, "hours:", population)
print("Organisms after", totalHours, "hours:", totalPopulation)
