def copy_file(file1, file2):
    with open(file1, "r", encoding="utf-8") as f1:
        cont1 = f1.read()
    with open(file2, "w", encoding="utf-8") as f2:
        f2.write(cont1)


copy_file(r"C:\Users\Amina\Desktop\тудасюда\song.txt", r"C:\Users\Amina\Desktop\тудасюда\karaoke.txt")