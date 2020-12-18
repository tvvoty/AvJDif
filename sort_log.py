import stats_log

# def findSmallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index
#
# def selectionSort(arr):
#     newArr = []
#     for i in range(len(arr)):
#         smallest = findSmallest(arr)
#         newArr.append(arr.pop(smallest))
#     return newArr


with open("F:\\GitHub\\AvJDif\\SubDif\\sorted_stats_log.py", mode='w', encoding='utf-8') as f:
    f.write('sorted_anime_avg_diff_table = {')
    for i in range(stats_log.diclen):
        smallest = 0
        line = ''
        for title, stats in stats_log.anime_avg_diff_table.items():
            if stats[2] < smallest:
                smallest = stats[2]
                line = f'"{title}" : [{stats}]' + '", \n"'
        f.write(line)
