starting_salary = float(input("Enter your starting salary (Do not include the $): "))
increase = float(input("Enter in yearly increase as a percentage (Do not include the % symbol): "))
years = int(input("Enter number of years as a teacher: ")) 

print("%-6s%-10s" % ("Year", "Salary"))

salary = starting_salary
for years in range(1, years + 1):
    print("%-6d%-10s" % (years, "$%0.2f" % salary))
    if years < 10:
        salary += salary * (increase / 100)

