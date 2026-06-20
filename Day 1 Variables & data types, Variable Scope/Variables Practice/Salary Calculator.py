basic_salary= int(input("Enter your basic salary: "))
bonus= int(input("Enter your bonus: "))
tax= int(input("Enter your tax: "))

net_salary= basic_salary + bonus - tax

print("net_salary",net_salary)
