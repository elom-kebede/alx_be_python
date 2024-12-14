monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_saving = monthly_income-monthly_expenses
A_saving = int(monthly_saving * 12 + (monthly_saving * 12 * 0.05))
print("Your monthly savings are $"+str(monthly_saving))
print("Projected savings after one year, with interest, is: $"+str(A_saving))
