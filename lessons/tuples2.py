tup = ("Spain", "Italy", "India", "England", "Germany")
print(tup)
#tuples are ichangable so we need to convert them to lists

#converting tuples to lists
temp = list(tup)
print(temp)

#appending the list
temp.append("Greece")

#converting lists back to tuples
tup = tuple(temp)


print(tup)

#however we can concanate tuples
tup1 = ("tarun","tanya")
tup2 = ("papa","mummy")
total = tup1 + tup2
print(total)

#since they are immutable it is limited to few methods on tuples
print(tup1.count("tarun"))

print(total.index("papa"))