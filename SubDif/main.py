from pysubparser import parser
import freq_dic
import MeCab
import os

# parse subtitles with MeCab
wakati = MeCab.Tagger("-Owakati")


# dir with subtitles
os.chdir("F:\GitHub\AvJDif\SubDif\subs\Barakamon")


def find_avg_diff_of_folder():
    sum_of_diff = 0
    wordcount = 0
    for file in os.listdir(os.getcwd()):
        file_path = (os.path.join(os.getcwd(), file))
        print(file_path)
        subtitles = parser.parse(file_path)
        print(subtitles)


        for subtitle in subtitles:
            print(subtitle.text)
            parsed_line = wakati.parse(subtitle.text).split()
            print(parsed_line)
            for word in parsed_line:
                print(word)
                for entry in freq_dic.freq_list:
                    if word == entry[0]:
                        wordcount += 1
                        sum_of_diff += entry[2]
                        print(entry[2])
    print(sum_of_diff)
    print(wordcount)
    print(sum_of_diff / wordcount)

find_avg_diff_of_folder()





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
