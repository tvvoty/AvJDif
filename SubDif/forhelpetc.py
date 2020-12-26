# file for testing purposes

folder = "nya"
# anime_avg_diff_table = [["Barakamon", 64398385, 28217, 2282], \n
#                         ["Barakamonwithzip", 471757, 30047, 2345],\n
#                         ["SSR", 37801167, 17446, 2166.7526653674195],\n
# #                         ["tsurezure", 118850576, 60931, 1950]]
# sum_of_diff = 4
# wordcount = 2
#
# print("{" + f'"{folder}" : [{sum_of_diff},{wordcount},{sum_of_diff / wordcount}]' + "}")


# print(f"folder : [2525, 12, 1245],\n folder : [2525, 12, 1245],\n folder : [2525, 12, 1245]")
# print(anime_avg_diff_table)


anime_avg_diff_table = {"Barakamon" : [64398385,28217,2282.25484636921],
"Barakamonwithzip" : [70471757,30047,2345.384131527274],
"empty" : [0,0,"Error in av_dif func in line 47"],
"SSR" : [37801167,17446,2166.7526653674195],
"tsurezure" : [118850576,60931,1950.576488158737]}

for p, d in anime_avg_diff_table.items():
    print( d)
