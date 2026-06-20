company_name = "Nandi_AI"

def employee_details():

    Name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    salary = float(input("Enter employee salary: "))

    annual_salary = salary*12

    print("Company Name", company_name)
    print("Name", Name)
    print("Age", age)
    print("Salary", salary)
    print("Annual salary", annual_salary)

employee_details()

