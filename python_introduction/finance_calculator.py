income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
M_saving = income-expenses
A_saving = M_saving * 12 +(M_saving * 12 * 0.05)
print("Your monthly savings are $",M_saving)
print("Projected savings after one year, with interest, is: $",A_saving)
