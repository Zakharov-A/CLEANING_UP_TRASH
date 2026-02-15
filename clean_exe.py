import os

directory_path = r'C:\Users\Boba\Downloads'

directory_content = os.listdir(directory_path)

for file_name in directory_content:
    if file_name.endswith('.exe'):
        os.remove(directory_path + '\\' + file_name)
        