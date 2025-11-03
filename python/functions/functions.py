def say():
    print("Hello World");

say();

# --------------

def checkingFunction(age, has_id):
    age = 20
    has_id = True

    if age >= 18:
        if has_id:
            print("You can enter.")
        else:
            print("You need an ID.")
    else:
        print("You are too young.")

age = 25;
has_id = True;

checkingFunction(age, has_id);

# --------------

def hello(name="Guest"):
    print("Hello" + name);

hello(); # print Guest
hello("Jeral");


# --------------
# Named arguments

def checkingFunction(age, has_id):
    age = 20
    has_id = True

    if age >= 18:
        if has_id:
            print("You can enter.")
        else:
            print("You need an ID.")
    else:
        print("You are too young.")


checkingFunction(age=25, has_id=False);


# --------------
# Return values

def add(a, b):
    result = a + b;
    return result;  # sends the result back to whoever called the function

sum_value = add(5, 3)
print(sum_value)  # Output: 8
