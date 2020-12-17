import glob
import os

main_folder = ("F:\\GitHub\\AvJDif\\SubDif\\sub_archive_simulation")

def find_avg_diff_of_folder_with_hashtable():
    for folder in os.listdir(main_folder):
        print(folder)
        sub_folder_path = f'{main_folder}\\{folder}'
        os.chdir(sub_folder_path)
        print(sub_folder_path)
        allfiles = glob.glob(f"{os.getcwd()}\\**\\**.**", recursive=True)
        print(f'All file in glob globe func are')
        for x in allfiles:
            mes = x
            print(x)

        # for file in os.listdir(os.getcwd()):
        for file in glob.glob(f"{os.getcwd()}\\*.*", recursive=True):
            file_path = (os.path.join(os.getcwd(), file))
            # print(file_path)
            # print(subtitles)

find_avg_diff_of_folder_with_hashtable()
