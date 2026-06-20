company = "OpenAI"

def show_company():
    print(company)

show_company()

#Questions:

# 1. Is `company` global or local?
# Global
# 2. Why does it work inside the function?
#because company is defined in the global scope, and Python allows functions to access global variables when no local variable with the same name exists.