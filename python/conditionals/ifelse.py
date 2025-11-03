
# if condition:
#     # code runs if condition is True
# elif another_condition:
#     # code runs if previous condition was False, but this one is True
# else:
#     # code runs if all above conditions are False

# If statement
age = 18

if age >= 18:
    print("You are an adult.")


# if + else statement
age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# if, elif, and else statement
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# Nested if statement
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("You can enter.")
    else:
        print("You need an ID.")
else:
    print("You are too young.")
