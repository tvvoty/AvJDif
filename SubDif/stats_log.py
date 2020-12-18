anime_avg_diff_table = {"Barakamon" : [64398385,28217,2282.25484636921],"Barakamonwithzip" : [70471757,30047,2345.384131527274],"empty" : [0,0,"Error in av_dif func in line 47"],"SSR" : [37801167,17446,2166.7526653674195],"tsurezure" : [118850576,60931,1950.576488158737]}

# sorted(anime_avg_diff_table, key=lambda x: (anime_avg_diff_table[x]['downloads'], anime_avg_diff_table[x]['date']))

diclen = (len(anime_avg_diff_table))


def log_sort():
    errorlist = []
    sorted = []
    with open("F:\\GitHub\\AvJDif\\SubDif\\sorted_stats_log.py", mode='w', encoding='utf-8') as f:
        f.write('sorted_anime_avg_diff_table = {')
        for i in range(len(anime_avg_diff_table)):
            print(f"It's cycle number {i}")
            biggest = 0
            print(f"Biggest is now: {biggest}")
            line = ''
            print(f"Line is now: {line}")
            for title, stats in anime_avg_diff_table.items():
                print(f"The av_dif of {title}: {stats[2]}")

                isSorted = title in sorted
                print(f"Title is in sorted: {isSorted}")
                if not isSorted:
                    try:
                        if int(stats[2]) > int(biggest):
                            biggest = stats[2]
                            print(f"Biggest now is {biggest}")
                            line = f'"{title}" : {stats}' + ", \n"
                            print(f"The line is:{line}")
                            sorted.append(title)
                            print(f"Sorted list is:{sorted}")
                        else:
                            print(f"{title} is not biggest that biggest")
                    except:
                        errorlist.append(line)
                        print(f"Appenging {line} to the errorlist")

                        sorted.append(title)
                        print(f"Sorted list is:{sorted}")
            f.write(line)
            print(f"Printig {line} into the file")
        for x in errorlist:
            f.write(x)

log_sort()
