x = [1, 2, 3, 4, 5];
y = [6, 7, 8, 9, 10];

# Zero index

# Access element
el = x[0];

# Change index value
x[0] = 25;

# Add element to end
x.append(6);

# Add element to a specific index
x.insert(2, 7); # index , value

# Remove element
x.remove(6); # value
x.pop(0); # index

# Combine lists
x + y;

# Delete whole list
x.clear();

# We can slice a list
y = x[0:2]; # Get 0 - 2 element