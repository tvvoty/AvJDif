from pysubparser import parser
import shit
import MeCab


#put there absolute path of the file with double slashes eg 'E:\PythonProjects\pythonProject1\Anime frec list\[Kamigami] Barakamon - 01 [1280×720 x264 AAC Sub(Chs,Jap)].ass'
sub_file = 'put there path of the file'
subtitles = parser.parse('E:\\PythonProjects\\pythonProject1\\Anime frec list\\[Kamigami] Barakamon - 01 [1280×720 x264 AAC Sub(Chs,Jap)].ass')

#test, works
# for subtitle in subtitles:
#     print(subtitle.text)

#parse subtitles with MeCab
wakati = MeCab.Tagger("-Owakati")

for subtitle in subtitles:
    print(subtitle.text)
    parsed_line = wakati.parse(subtitle.text).split()