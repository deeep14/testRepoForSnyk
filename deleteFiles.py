import os

def delete_files():
    directory = input("Enter the directory path to delete files: ")
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            os.remove(filename)
    print("Files deleted successfully!")

delete_files()
