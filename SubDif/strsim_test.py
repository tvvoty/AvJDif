from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

a = similar("7 Seeds","A[Erai-raws] 7 Seeds - 01 [720p][Multiple Subtitle]")
print(a)
