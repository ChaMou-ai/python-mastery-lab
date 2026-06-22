import sys

num1 = int(sys.argv[1])
operator = sys.argv[2]
num2 = int(sys.argv[3])

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Operator Not Supported")

