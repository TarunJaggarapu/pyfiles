dict = {"tarun":"teja",
        "Sasuke" : "uchiha",
        "uzumaki" : "naruto",
         "Sasi": "kunar",
         "hyuga": {"hinata":"neji"},
         "rank": [12,332,43]}
print(dict.items())
print(dict["hyuga"]["hinata"])
print(dict.keys())
print(dict.values())
dict1 = {"iphone": "apple","samsung": "andriod"}
dict.update(dict1)
print(dict)

l = [3,4,13,6,2,5,2,3,1]
l1 = []
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)
#or
s = list(set(l))
print(s)