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
    for filename in os.listdir(os.getcwd()):
        filepath = (os.path.join(os.getcwd(), filename)
        subtitles = parser.parse(filepath)

        # for every line in the file
        for subtitle in subtitles:
            print(subtitle.text)
            # print(subtitle.text.encode("utf-8"))
            parsed_line = wakati.parse(subtitle.text).split()
            print(parsed_line)
            # print(parsed_line.encode("utf-8"))
            for word in parsed_line:
                print(word)
                # print(word.encode("utf-8"))
                for entry in freq_dic.freq_list:
                    if word == entry[0]:
                        wordcount += 1
                        sum_of_diff += entry[2]
                        print(entry[2])
    print(sum_of_diff)
    print(wordcount)
    print(sum_of_diff / wordcount)

find_avg_diff_of_folder()





def dum():
    # test
    # for subtitle in subtitles:
    #     print(subtitle.text)
    pass








# old function for one file
def find_avg_diff():
    sum_of_diff = 0
    wordcount = 0
    # for every line in the file
    for subtitle in subtitles:
        print(subtitle.text)
        # print(subtitle.text.encode("utf-8"))
        parsed_line = wakati.parse(subtitle.text).split()
        print(parsed_line)
        # print(parsed_line.encode("utf-8"))
        for word in parsed_line:
            print(word)
            # print(word.encode("utf-8"))
            for entry in freq_dic.freq_list:
                if word == entry[0]:
                    wordcount += 1
                    sum_of_diff += entry[2]
                    print(entry[2])
    print(sum_of_diff)
    print(wordcount)
    print(sum_of_diff / wordcount)
