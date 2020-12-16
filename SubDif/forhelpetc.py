import os

# help(os)
a = "a"
b="b"
c="c"
d="d"
with open("F:\\GitHub\\AvJDif\\SubDif\\stats_log.txt", mode='w', encoding='utf-8') as f:
    f.write('anime_avg_diff_table = ')

print('eee')

with open("F:\\GitHub\\AvJDif\\SubDif\\stats_log.txt", mode='w', encoding='utf-8') as f:
    f.write(f'[{a},{b},{c},{d}], ')
