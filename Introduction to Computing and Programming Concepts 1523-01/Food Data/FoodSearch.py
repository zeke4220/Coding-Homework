
    # Open the file
with open('FoodValues.txt', 'r') as file:
        # Read each line in the file
    for line in file:
            # Split the line into parts
        parts = line.strip().split(' ')  # Adjust the delimiter if needed

            # Assign parts to variables
            # Ensure that there are enough parts in the line to unpack
        if len(parts) >= 3:
            var1, var2, var3 = parts[0], parts[1], parts[2]
                # Do something with the variables
            print(var1, var2, var3)
        else:
            print(f"Line '{line.strip()}' does not have enough parts.")
