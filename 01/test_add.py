from main import add

print("Failed on two positive numbers", add(1, 2) == 3)
print("Failed on one positive and one negative number", add(-1, 2) == 1)
print("Failed on two negative numbers", add(-1, -2) == -3)
print("Failed on adding zero", add(0, 5) == 5)
print("Failed on adding zero", add(5, 0) == 5)
print("Failed on adding two zeros", add(0, 0) == 0)


print("Failed on two positive numbers", add("1", 2) is None)
