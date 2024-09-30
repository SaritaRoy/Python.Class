#4.Write a program to saved a list object into a file and read the same file and recover as list without using pickle module.
def save_list_to_file(data_list, filename):
    """
    Save a list to a text file.

    Parameters:
    data_list (list): The list to be saved.
    filename (str): The name of the file to save the list to.

    Returns:
    None
    """
    with open(filename, 'w') as file:
        for item in data_list:
            file.write(f"{item}\n")  # Write each item on a new line

    print("List saved successfully.")

def load_list_from_file(filename):
    """
    Load a list from a text file.

    Parameters:
    filename (str): The name of the file to load the list from.

    Returns:
    list: The loaded list.
    """
    loaded_list = []
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                loaded_list.append(line.strip())  # Add each line to the list after stripping whitespace
        
        print("List loaded successfully.")
        return loaded_list
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6]
    save_list_to_file(my_list, "my_list.txt")
    
    recovered_list = load_list_from_file("my_list.txt")
    print("Recovered List:", recovered_list)
