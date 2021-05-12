# main file with all the functions

from pysubparser import parser  # parses subtitle files, now that i think about it, it's prolly unnecesary since
# mecab parses every thing anyway
import freq_dic_hashtable  # A hash table with difficulty of words, created from
import MeCab  # Parses japanese text
import os
import glob

# finds avg_diff of every title in a folder with nested filders
def find_avg_diff_of_folder_with_hashtable():
    for folder in os.listdir(main_folder):
        print(folder)
        sub_folder_path = f'{main_folder}\\{folder}'
        os.chdir(sub_folder_path)
        print(sub_folder_path)
        sum_of_diff = 0
        wordcount = 0
        allfiles = glob.glob(f"{os.getcwd()}\\*.*", recursive=True)
        print(f'All file in glob globe func are')
        for x in allfiles:
            mes = x
            print(x)

        # for file in os.listdir(os.getcwd()):
        for file in glob.glob(f"{os.getcwd()}\\**\\**.**", recursive=True):
            file_path = (os.path.join(os.getcwd(), file))
            print(file_path)
            try:
                subtitles = parser.parse(file_path)
                # print(subtitles)

                for subtitle in subtitles:
                    # print(subtitle.text)
                    parsed_line = wakati.parse(subtitle.text).split()
                    # print(parsed_line)
                    for word in parsed_line:
                        # print(word)
                        if word in freq_dic_hashtable.freq_hashtable:
                            wordcount += 1
                            sum_of_diff += freq_dic_hashtable.freq_hashtable[word]
                            # print(freq_dic_hashtable.freq_hashtable[word])
            except:
                print("Wrong file format.")
        # print(sum_of_diff)
        # print(wordcount)
        try:
            print(sum_of_diff / wordcount)
            f.write(f'"{folder}" : [{sum_of_diff},{wordcount},{sum_of_diff / wordcount}]' + ", \n")
        except:
            print("Error, prolly division by zero, prolly not important.")
            f.write(f'"{folder}" : [{sum_of_diff},{wordcount},\"Error in av_dif func in line 47\"]' + ", \n")





# parse subtitles with MeCab
wakati = MeCab.Tagger("-Owakati")

# main_folder = ("F:\\GitHub\\AvJDif\\SubDif\\sub_archive_simulation")
main_folder = ("F:\Afordearch")
with open("F:\\GitHub\\AvJDif\\SubDif\\stats_log.py", mode='w', encoding='utf-8') as f:
    f.write('anime_avg_diff_table = {')

    find_avg_diff_of_folder_with_hashtable()

with open("F:\\GitHub\\AvJDif\\SubDif\\stats_log.py", 'rb+') as f:
    f.seek(-4, os.SEEK_END)
    f.truncate()

with open("F:\\GitHub\\AvJDif\\SubDif\\stats_log.py", mode='a', encoding='utf-8') as f:
    f.write('}')








# def find_avg_diff_of_folder():
#     sum_of_diff = 0
#     wordcount = 0
#     for file in os.listdir(os.getcwd()):
#         file_path = (os.path.join(os.getcwd(), file))
#         print(file_path)
#         subtitles = parser.parse(file_path)
#         print(subtitles)
#
#
#         for subtitle in subtitles:
#             print(subtitle.text)
#             parsed_line = wakati.parse(subtitle.text).split()
#             print(parsed_line)
#             for word in parsed_line:
#                 print(word)
#                 for entry in freq_dic.freq_list:
#                     if word == entry[0]:
#                         wordcount += 1
#                         sum_of_diff += entry[2]
#                         print(entry[2])
#     print(sum_of_diff)
#     print(wordcount)
#     print(sum_of_diff / wordcount)




# def dum():
#     # test
#     # for subtitle in subtitles:
#     #     print(subtitle.text)
#     pass








# old function for one file
# def find_avg_diff():
#     sum_of_diff = 0
#     wordcount = 0
#     for subtitle in subtitles:
#         print(subtitle.text)
#         parsed_line = wakati.parse(subtitle.text).split()
#         print(parsed_line)
#         for word in parsed_line:
#             print(word)
#             for entry in freq_dic.freq_list:
#                 if word == entry[0]:
#                     wordcount += 1
#                     sum_of_diff += entry[2]
#                     print(entry[2])
#     print(sum_of_diff)
#     print(wordcount)
#     print(sum_of_diff / wordcount)
