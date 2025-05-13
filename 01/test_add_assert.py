from main import add

# Test two positive numbers
assert add(1, 2) == 3, "Failed on two positive numbers"

# Test one positive and one negative number
assert add(-1, 2) == 1, "Failed on one positive and one negative number"

# Test two negative numbers
assert add(-1, -2) == -3, "Failed on two negative numbers"

# Test adding zero
assert add(0, 5) == 5, "Failed on adding zero"
assert add(5, 0) == 5, "Failed on adding zero"

# Test adding two zeros
assert add(0, 0) == 0, "Failed on adding two zeros"
