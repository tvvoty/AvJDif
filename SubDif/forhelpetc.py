import os

# help(os)

main_folder = ("F:\GitHub\AvJDif\SubDif\sub_archive_simulation")

for folder in os.listdir(main_folder):
    sub_folder_path = f'{main_folder}\\{folder}'
    os.chdir(sub_folder_path)
    print(folder)
    print(sub_folder_path)
