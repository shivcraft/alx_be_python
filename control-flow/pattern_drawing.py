# pattern_drawing.py
# Prompt the user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row=0
# Use a while loop for each row
while row < size:
    # Use a for loop to print '*' in each column
    for col in range(size):
        print('*', end=' ')
    # Move to the next line after each row
    print()
    row += 1

