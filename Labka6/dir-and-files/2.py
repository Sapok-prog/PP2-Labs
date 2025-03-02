import os


def check_path_access(path):
    print(f"Checking path called:{path}")
    if os.path.exists(path):
        print(f"Path exists")
    else:
        print(f"Path doesn't exist")
        return

    if os.access(path, os.W_OK):
        print(f"The path is writeable")
    else:
        print("THe path isn't writeable")

    if os.access(path, os.R_OK):
        print(f"The path is readable")
    else:
        print("THe path isn't readable")

    if os.access(path, os.X_OK):
        print(f"The path is executable")
    else:
        print("THe path isn't executable")


check_path_access(r'C:\Users\Amina\Desktop\тудасюда')