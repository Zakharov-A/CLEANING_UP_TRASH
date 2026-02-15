import os

directory_path = r'C:\Users\Boba\Pictures\Screenshots'

directory_content = os.listdir(directory_path)

for file_name in directory_content:
    if file_name.endswith('.png'):
        os.remove(os.path.join(directory_path, file_name))
        
        