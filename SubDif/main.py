from pysubparser import parser
import shit
import MeCab


#put there absolute path of the file with double slashes eg 'E:\PythonProjects\pythonProject1\Anime frec list\[Kamigami] Barakamon - 01 [1280×720 x264 AAC Sub(Chs,Jap)].ass'
sub_file = 'put there path of the file'
subtitles = parser.parse('E:\\PythonProjects\\pythonProject1\\Anime frec list\\Psycho-Pass_001.srt')

#test, works
# for subtitle in subtitles:
#     print(subtitle.text)

#parse subtitles with MeCab
wakati = MeCab.Tagger("-Owakati")


def find_avg_diff():
    sum_of_diff = 0
    wordcount = 0
    # for every line in the file
    for subtitle in subtitles:
        print(subtitle.text)
        parsed_line = wakati.parse(subtitle.text).split()
        print(parsed_line)
        for word in parsed_line:
            print(word)
            for entry in shit.shitlist:
                if word == entry[0]:
                    wordcount += 1
                    sum_of_diff += entry[2]
                    print(entry[2])
    print(sum_of_diff)
    print(wordcount)
    print(sum_of_diff / wordcount)


                # else:
                #     print("no")
        #         print(shit.shitlist.index(word))


find_avg_diff()



