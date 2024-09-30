#3.Create a function to perform the above tasks, explain the function using docstring, add asserts statement, to catch possible errors, add comments to explain workflow and function methods/modules used.  
import pickle

def save_object(obj, filename):
    
    assert isinstance(filename, str), "The filename must be a string."
    assert obj is not None, "The object cannot be None and must be serializable."

    try:
        with open(filename, 'wb') as file:
            pickle.dump(obj, file)
            print("Object saved successfully.")
    
    except Exception as e:
        print(f"Error in saving the object: {e}")

def load_object(filename):
   
    assert isinstance(filename, str), "The filename must be a string."

    try:
        with open(filename, 'rb') as file:
            obj = pickle.load(file)
            print("Object loaded successfully.")
            return obj

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred while loading the object: {e}")

if __name__ == "__main__":
    new_data = {"Name": "Sarita", "Age": 20}
    save_object(new_data, "data.pickle")
    loaded_data = load_object("data.pickle")
    print("Loaded Data:", loaded_data)
