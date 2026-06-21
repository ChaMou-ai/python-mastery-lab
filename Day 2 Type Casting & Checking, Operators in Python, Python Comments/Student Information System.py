name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))
total_marks = 500

percentage = (marks / total_marks ) * 100

passed = percentage >= 40
scholarship = percentage >= 80
print("***** Students Reporting *****")
print("Your name is ", name)
print ("Your age is ", age)
print ("Your marks is ", marks)
print ("Your percentage is ", percentage)

if passed:
    print("Result:  Pass")
else:
    print("Result:  Fail")
if scholarship:
    print("you are eligible for Scholarship")
else:
    print("you are not eligible for Scholarship")


print("***** END *****")


print(type(name))
print(type(age))
print(type(marks))

