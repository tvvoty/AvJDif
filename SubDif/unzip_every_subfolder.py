# file to unzip every zip in a folder
import shutil
import glob
import os

# main_folder = ("F:\\GitHub\\AvJDif\\SubDif\\sub_archive_simulation")
main_folder = ("C:\\Users\\Windows 8.1\\Desktop\\csstemp")
# main_folder = ("F:\Afordearch")
# os.chdir(main_folder)
# print(os.listdir())

def unzip_all_subfolders():
    for folder in os.listdir(main_folder):
        # print(folder)
        sub_folder_path = f'{main_folder}\\{folder}'
        os.chdir(sub_folder_path)
        # print(sub_folder_path)

        for zip_file in glob.glob(f"{os.getcwd()}\\*.zip"):
            try:
                shutil.unpack_archive(zip_file, os.getcwd())
                # file_path = (os.path.join(os.getcwd(), file))
                os.remove(zip_file)
                print(zip_file)
            except:

                print("Error")
                os.remove(zip_file)

unzip_all_subfolders()


# zips = glob.glob("F:\\GitHub\\AvJDif\\SubDif\\sub_archive_simulation\\Barakamonwithzip\\*.zip")
#
# print(f"Zip files are: {zips}")
