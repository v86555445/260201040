books = ["ULYSSES", "ANIMAL FARM", "BRAVE NEW WORLD", "ENDER'S GAME"]
d = dict()


for i in books:
    e = set()
    for j in i:
        e.add(j)
    d[i] = (len(i), len(e),(len(i)+len(e))/2)
print(d)

