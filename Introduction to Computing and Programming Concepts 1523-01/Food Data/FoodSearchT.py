
def search_and_extract_values(file_path, search_terms):
    """
    Searches for specific terms in a given file and extracts their protein, fat, and calorie values.

    :param file_path: Path to the file to be searched.
    :param search_terms: List of terms to search for in the file.
    :return: Dictionary with each search term as key and a dictionary of its protein, fat, and calorie values.
    """
    search_results = {term: {'Proteins': None, 'Fat': None, 'Calories': None} for term in search_terms}

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for term in search_terms:
            for line in lines:
                if term.lower() in line.lower():
                    # Extract and assign values for proteins, fat, and calories
                    # Assuming each line has a consistent format for these values
                    line_parts = line.split()  # Split the line into parts
                    try:
                        search_results[term]['Proteins'] = line_parts[-3]  # Assuming third-last value is protein
                        search_results[term]['Fat'] = line_parts[-2]      # Assuming second-last value is fat
                        search_results[term]['Calories'] = line_parts[-1] # Assuming last value is calories
                    except IndexError:
                        # Handle the case where the line does not have enough parts
                        search_results[term] = {'Proteins': 'Not found', 'Fat': 'Not found', 'Calories': 'Not found'}
                    break  # Stop searching once the term is found

    return search_results

# Define the file path and the search terms
file_path = 'Elements.txt'
search_terms = [
    "Scrambled Eggs",
    "Ham Sliced Regular",
    "Bread Whole Wheat Toasted",
    "Baked Beans",
    "Orange Juice",
    "Sauerkraut",
    "Pickled Beets"
]

# Perform the search and extract values
search_results = search_and_extract_values(file_path, search_terms)
search_results

