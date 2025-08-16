import shutil
import os
import re

new_dir = "C:\\Users\\pdhanush\\Downloads\\Complete-Python-3-Bootcamp-master\\Complete-Python-3-Bootcamp-master\\12-Advanced Python Modules"
zip_pattern = re.compile(r'\.zip$')
txt_pattern = re.compile(r'\.txt$')
new_file_name = 'Puzzle'

for folders,sub_folders,files in os.walk(new_dir):
    for filename in files:
        if zip_pattern.search(filename):
            shutil.unpack_archive(os.path.join(folders, filename),new_file_name,'zip')

current_dir = os.getcwd()
instructions_file_path = '' 

flag = False
for folder,sub_folders,files in os.walk(current_dir):
    for filename in files:
        if re.search(txt_pattern, filename):
            instructions_file_path = os.path.join(folder, filename)
            flag = True
            break
    if flag:
        break

print(instructions_file_path)

with open(instructions_file_path, 'r') as file:
    instructions = file.read()
    print(instructions)