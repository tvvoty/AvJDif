# converts a nested list dic into a hashtable

import freq_dic

freq_hashtable = {entry[0]: entry[2] for entry in freq_dic.freq_list}

# for entry in freq_dic.freq_list:
#     d = {entry[0] : entry[1:]}

with open('freq_dic_hashtable.py', 'w', encoding='utf-8') as f:
    f.write(f'freq_hashtable = {freq_hashtable}')
