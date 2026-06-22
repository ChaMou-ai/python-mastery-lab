import sys

height = float(sys.argv[1])
weight = float(sys.argv[2])
height_m = height / 100
bmi = weight / (height_m ** 2 )

print(f"bmi:",bmi)
print(f"height:",height)
print(f"weight:",weight)

