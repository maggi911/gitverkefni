# Make a variable called max_int and set value to num_int
# Use while loop to ask user to input new number, until a negative value is entered
# Compare new number to max_int with if sentence
# If the new number is higher than current max_int, set max_int value as the new number
# When user inputs a negative integer, print out the value of max_int


num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
max_int = num_int

while num_int >= 0:
    num_int = int(input("Input a number: "))
    if num_int > max_int:
        max_int = num_int
else:
    print("The maximum is", max_int)    # Do not change this line