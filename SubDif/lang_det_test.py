from langdetect import detect
from langdetect import detect_langs
a = detect("War doesn't show who's right, just who's left.")
print(a)
#
a = detect("Ein, zwei, drei, vier")

print(a)

a = detect("Сука")
print(a)

a = detect("Сука")
print(a)


a = detect("あのう　なんて言ってるか分かんないんですけど")
print(a)


a = detect("哼 能別拿我跟那個變態四眼相提並論嗎")
print(a)

a = detect_langs("哼 能別拿我跟那個變態四眼相提並論嗎 あのう　なんて言ってるか分かんないんですけど")
print(a)
import pycl
