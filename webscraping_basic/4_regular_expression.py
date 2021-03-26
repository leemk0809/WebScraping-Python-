import re
# abcd, book, desk
# ca?e
# care, cafe, case, cave
# caae, cabe, cace, cade, ...

p = re.compile("ca.e") 
# . (ca.e) : 一文字を意味 > care, cafe, case (o) | caffe (x)
# ^ (^de) : 文字列の初め > desk, description(o) | fade (x)
# $ (se$) : 文字列の末> case,base (o) | face(x)

def print_match(m):
    if m:
        print("m.gorup() : ", m.group()) #一致する文字列の返還
        print("m:string : ", m.string) #入力してくれた文字列
        print("m.start() : ", m.start()) #一致する文字列の最初index
        print("m.end() : ", m.end()) #一致する文字列の末index
        print("m.span() : ", m.span()) #一致する文字列の最初と末index
    else:
        print("マッチが出来ません。")
#print(m.group()) #マッチが出来ないとエラー発生

# m = p.match("careless") # match : 文字列が最初から一致するか確認 -> care
# print_match(m)

# m = p.search("good care") # search : 文字列の中に一致する物があるか確認 -> care
# print_match(m)

# lst = p.findall("good care cafe") # findall : 一致する全てを'リスト'形で返還　-> care, cafe
# print(lst)

# 1. p = re.compile("value")
# 2. m = p.match("value")
# 3. m = p.search("value")
# 4. lst = p.findall("value")