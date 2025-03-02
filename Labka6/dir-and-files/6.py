def A_Z_files():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for x in letters:
        file_name = f"{x}.txt"
        with open(file_name, "w") as file:
            file.write(f" This is file {file_name} ")


A_Z_files()