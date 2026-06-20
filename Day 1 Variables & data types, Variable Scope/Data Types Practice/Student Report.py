

name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
total_marks = int(input("Enter your total marks: "))

percentage = (marks / total_marks) * 100

passed = percentage >= 40


print("/n **** Student Report ****")
print ("Enter your name", name)
print ("Enter your mark", marks)
print ("Enter your total mark", total_marks)

print ("percentage", percentage)
print ("Result", passed)



