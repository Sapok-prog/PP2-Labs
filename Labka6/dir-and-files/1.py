import os
import os


def list_dir(path):
    if not os.path.exists(path):
        print(f"The specified path '{path}' does not exist.")
        return
    directory = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    all_items = os.listdir(path)

    print(f"All directories are {directory}")
    print(f"All files are {files}")
    print(f"List of all directories and files {all_items}")
    return


path_file = r'C:\Users\Amina\Desktop\тудасюда'
list_dir(path_file)
