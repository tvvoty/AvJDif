# file to sort list of titles with thier avg_diff stuts
import stats_log
import os




def log_sort(usorted_avg_diff_table):
    # list of all titles that threw an error
    errorlist = []

    # list of sorted titles to chek it later
    sorted = []

    with open("sorted_stats_log.py", mode='w', encoding='utf-8') as f:
        print(f"creating log file in the {os.getcwd()}")
        f.write('sorted_anime_avg_diff_table lol = {')
        print(f'Table list length: {len(usorted_avg_diff_table)}')

        # start cycle to check every title
        for i in range(len(usorted_avg_diff_table)):

            print(f"It's cycle number {i + 1} \n")
            # line for error titles
            errorline = ""
            # the title of the biggest title
            bigest_title = ""
            # avg_diff of a title with the biggest avg_diff so far in the cycle
            biggest = 0
            print(f"Biggest is now: {biggest}")
            # Line to write in the file of the title with the biggest avg_diff
            line = ''
            print(f"Line is now: {line} \n")

            print("Start cheking titles in hash table \n")
            # start cycle cheking every title in the Table
            for title, stats in usorted_avg_diff_table.items():
                print(f"The av_dif of {title}: {stats[2]}")

                #Checking if the title is in sorted list
                isSorted = title in sorted
                print(f"In sorted: {isSorted}")

                # if not in sorted > check if title's avg_diff bigger than biggest so far
                if not isSorted:
                    try:
                        if int(stats[2]) > int(biggest):
                            print(f"{title}: ({stats[2]}) is bigger than {biggest}")
                            biggest = stats[2]
                            bigest_title = title
                            print(f"Biggest now is {bigest_title}: ({biggest})")
                            line = f'"{title}" : {stats}' + ", \n"
                            print(f"The line is:{line} \n")
                        else:
                            print(f"{title}: ({stats[2]}) is not bigger than {bigest_title}: ({biggest}) \n")

                    # if titles stat contain a string with an error > append it to the error list
                    except:
                        errorline = f'"{title}" : {stats}' + ", \n"
                        errorlist.append(errorline)

                        print(f"Title have an error, appenging {line} to the errorlist")
                        sorted.append(title)
                        print(f"Sorted list is:{sorted} \n")

            # appendig biggist line on the cycle to the sorted list
            sorted.append(bigest_title)
            print(f"Appendig {bigest_title} to the sorted")
            print(f"Sorted list is now:{sorted}")

            # write the line of the title with the biggest avg_diff to the file
            f.write(line)
            print(f"Printig {line} into the file")

        # after all the operation write all errored titles to the end
        for errortitle in errorlist:
            f.write(errortitle)

    print("Deleting (,)")
    with open("sorted_stats_log.py", 'rb+') as f:
        f.seek(-4, os.SEEK_END)
        f.truncate()

    print("Appending }")
    with open("sorted_stats_log.py", mode='a', encoding='utf-8') as f:
        f.write('}')

log_sort(stats_log.anime_avg_diff_table)
