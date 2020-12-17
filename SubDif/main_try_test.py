from pysubparser import parser
import freq_dic
import freq_dic_hashtable
import MeCab
import os
import glob


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
        print(sum_of_diff / wordcount)
        f.write(f'[{folder},{sum_of_diff},{wordcount},{sum_of_diff / wordcount}], ')



# parse subtitles with MeCab
wakati = MeCab.Tagger("-Owakati")

main_folder = ("F:\\GitHub\\AvJDif\\SubDif\\sub_archive_simulation")
with open("F:\\GitHub\\AvJDif\\SubDif\\stats_log.txt", mode='w', encoding='utf-8') as f:
    f.write('anime_avg_diff_table = ')

    find_avg_diff_of_folder_with_hashtable()








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
