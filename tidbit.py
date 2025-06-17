purchase_price = float(input("Please enter purchase price without the $: "))
down_payment = .10 * purchase_price
starting_balance = purchase_price - down_payment
balance = starting_balance
interest_rate = .12
interest = (balance * interest_rate)/12
monthly_payment = .05 * purchase_price
principle = monthly_payment - interest

print("%-6s%10s%10s%10s%10s%10s" % ("Month", "Balance", "Interest", "Principle", "Payment", "Remaining"))

month = 1

while balance > 0:
    principle = monthly_payment - interest
    interest = (balance * interest_rate)/12
    if principle > balance:
        principle = balance
        monthly_payment = interest + principle
    remaining = balance - principle
    print("%-6d%10.2f%10.2f%10.2f%10.2f%10.2f" % (month, balance, interest, principle, monthly_payment, remaining))
    balance = remaining
    month += 1
