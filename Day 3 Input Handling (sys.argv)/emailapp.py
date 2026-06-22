import sys

full_name = sys.argv[1]
last_name = sys.argv[2]

if len(sys.argv) == 2:
    print("usage: python emailapp.py full_name last_name")
    sys.exit()

email = full_name.lower().replace(" ", "@")+last_name.lower() + "@company.com"

print("\n ---- Your Profile ----")
print("Name: " + full_name)
print("Last Name: " + last_name)
print("Email: " + email)