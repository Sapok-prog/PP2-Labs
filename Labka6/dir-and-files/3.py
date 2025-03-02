import os

def check(path):
    if not (os.path.exists(path)):
        print("Path doesn't exist")
        return
    print(f"{path} , Path exists")
    
    print(f"Directory: {os.path.dirname(path)}")
    print(f"Filename: {os.path.basename(path)}")


check(r"C:\Users\Amina\Desktop\тудасюда")
        