user = int(input("Enter a number to see its multiplication table:"))
for i in range(1,11):
    res = user * i
    print(user, "*", i, "=", res)