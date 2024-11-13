
def read_elements(filename):
    elements = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # Skip lines that do not contain data values or header information
            if "ID\tname\tFood Group\tCalories\tFat (g)\tProtein (g)\tCarbohydrate (g)\tSugars (g)\tFiber (g)\tCholesterol (mg)\tSaturated Fats (g)" in line:
                continue
            
            # Split the line into individual values
            values = line.strip().split('\t')
            
            # Check if the line has the expected number of values
            if len(values) == 11:
                # Create a dictionary for each element
                element = {
                    'Name': values[0],
                    'Calories': float(values[1]),
                    'Fat': float(values[4]) if values[2] != 'NULL' else None,
                    'Protein': float(values[5]) if values[3] != 'NULL' else None,
                    'Saturated Fats': float(values[10]) if values[4] != 'NULL' else None,
                }
                
                # Append the element to the list
                elements.append(element)
            else:
                print(f"Skipping invalid line: {line}")

    return elements

def search_food(elements, food_name):
    # Search for the exact given food name in the list of elements, regardless of capitalization
    results = [element for element in elements if element['Name'].lower() == food_name.lower()]
    
    return results

def main():
    filename = 'Elements.txt'
    elements = read_elements(filename)

    # Ask the user for the number of foods they want to look up
    num_foods = int(input("How many foods do you want to look up? "))

    for _ in range(num_foods):
        # Ask for the food name
        food_name = input("Enter the name of the food item: ")
        search_result = search_food(elements, food_name)
        
        if search_result:
            print(f"\nSearch Results for {food_name}:")
            for result in search_result:
                # Print each element of the food item
                for key, value in result.items():
                    print(f"{key}: {value}")
        else:
            print(f"No results found for {food_name}.")

if __name__ == "__main__":
    main()
