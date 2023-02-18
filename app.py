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
#converting lists into dictionary
d1 = ["tarun","teja","jagga"]
d2 = [1,2,3]
dict = {}
for i in range(len(d1)):
    dict[d1[i]] =d2[i]
print(dict) 

string = "tarunteja"
print(string.upper())
print(string.lower())

ls = [3,4,13,6,2,5,2,3,1]
sum = 0
for i in ls:
    sum = sum + i
print(sum)