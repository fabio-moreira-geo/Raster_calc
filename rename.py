from hashlib import new
import os

path = os.chdir(r'C:\Users\Usuario\Desktop\Imagens\B4')


for file in os.listdir(path):
    new_file_name = f"B04{file[19:]}"
    os.rename(file, new_file_name)
