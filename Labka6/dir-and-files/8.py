import os

def del_by_path(path):

    if os.path.exists(path) and os.access(path, os.R_OK):
        print(f"Path exists and accessible")
        os.remove(path)
        print("File has been removed successfully")

    else:
        print(f"Path doesn't exist")
        return