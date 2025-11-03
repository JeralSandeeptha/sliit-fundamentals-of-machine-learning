# Dictionary is like a object
# Has key value pairs

# Basic structure
x = {
    "name": "Jeral",
    "age": 25
};

# Add key
x["address"] = "Ragama";

# Access key
name = x['name'];

# Modify key
x["age"] = 1000;

# Get keys
x.keys();

# Get values
x.values();

# Access elements by order
x.get(1); # output: name

# Delete key
del x["name"];

# Delete whole dictionary
x.clear();