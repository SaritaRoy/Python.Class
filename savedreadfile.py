#Write another program to read the saved files to recover saved object and verify.
import pickle

fileName = "data_pickle"

try:
    
    with open(fileName, "rb") as fileHandle:
    
        list2 = pickle.load(fileHandle)
    
    print("Object loaded successfully.")
    print("Loaded List:", list2)

    list1 = [1, 2, 3, 4, 5, 6]

    
    if list1 == list2:
        print('Verification Successful: The loaded list matches the original list.')
    else:
        print('Verification Failed: The loaded list does not match the original list.')

except FileNotFoundError:
    print('File not found. Please ensure the file exists.')
except Exception as e:
    print(f'An error occurred while loading the object: {e}')
