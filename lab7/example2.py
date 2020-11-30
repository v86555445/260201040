books = ["ULYSSES", "ANIMAL FARM", "BRAVE NEW WORLD", "ENDER'S GAME"]
d = dict()
e = set()

for i in books:
    for j in i:
        e.add(j)
    d[i] = (len(i), len(e))
print(d)
