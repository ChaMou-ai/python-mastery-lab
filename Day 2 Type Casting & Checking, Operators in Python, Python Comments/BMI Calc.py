name = input("Enter your name: ")
age = input("Enter your age: ")
height_cm = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

height = height_cm / 100
bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "obese"
else:
    category = "overweight"

print("#### BMI ####")
print("name", name)
print("age", age)
print("height", height)
print("weight", weight)
print("bmi", bmi)
print("category", category)
print("#### END ####")
