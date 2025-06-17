hourly_wage = float(input("Please input your hourly wage: "))
overtime_pay = hourly_wage * 1.5
total_regular_hours = float(input("Please input your total regular hours: "))
total_overtime_hours = float(input("Please input your total overtime hours: "))
total_overtime_pay = total_overtime_hours * overtime_pay
weekly_pay = hourly_wage * total_regular_hours + total_overtime_pay
print(f"Employee's total weekly pay is: ${weekly_pay:.2f}") #Rounding to 2 decimals will make this look better
