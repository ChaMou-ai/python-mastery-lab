import sys

numbers = [int(num) for num in sys.argv[1:]]

print("total",sum(numbers))
