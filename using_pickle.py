#Write a program to read list and dictionary using pickle module
import pickle


list1 = [1, 2, 3, 4, 5, 6]


fileName = "data_pickle"

try:
    # Open the file in write binary mode
    with open(fileName, "wb") as FileHandle:
        # Save the list using pickle
        pickle.dump(list1, FileHandle)
        print("Object saved successfully.")
except Exception as e:
    print(f"An error occurred: {e}")