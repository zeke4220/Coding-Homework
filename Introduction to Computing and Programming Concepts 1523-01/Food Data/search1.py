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
                    'ID': values[0],
                    'Name': values[1],
                    'Food Group': values[2],
                    'Calories': float(values[3]),
                    'Fat': float(values[4]) if values[4] != 'NULL' else None,
                    'Protein': float(values[5]) if values[5] != 'NULL' else None,
                    'Carbohydrate': float(values[6]) if values[6] != 'NULL' else None,
                    'Sugars': float(values[7]) if values[7] != 'NULL' else None,
                    'Fiber': float(values[8]) if values[8] != 'NULL' else None,
                    'Cholesterol': float(values[9]) if values[9] != 'NULL' else None,
                    'Saturated Fats': float(values[10]) if values[10] != 'NULL' else None,
                }
                
                # Append the element to the list
                elements.append(element)
            else:
                print(f"Skipping invalid line: {line}")

    return elements

def search_food(elements, food_name):
    # Search for the given food name in the list of elements
    results = [element for element in elements if food_name.lower() in element['Name'].lower()]
    
    return results

def main():
    filename = 'Elements.txt'
    elements = read_elements(filename)

    # Example: Search for a specific food
    search_result = search_food(elements, 'Buttermilk')
    print("\nSearch Results:")
    for result in search_result:
        print(result)

if __name__ == "__main__":
    main()
