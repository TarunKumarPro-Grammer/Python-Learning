#<listname>.sort() sorts the list in ascending order , if wanted to sort in descending order, put reverse=True

list = [5,3,2,4,1,6]
# print(list)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)


#we can sort strings too

# list1 = ['e','d','c','b','a','f']
# print(list1)
# list1.sort()
# print(list1)
# list1.sort(reverse=True) is different from reverse() --> reverses the list



listName = ["kanya","tarun","chandra","tarun"]
# listName.reverse()
# print(listName)
# listName.sort()
# print(listName)

# print(listName.index("tarun"))
# print(listName.count("tarun"))

#we can copy list as well without modifying the original

newList = listName.copy()
# print(len(newList))
# newList.insert(0,"ramkishor") #<listname>.insert(index,listitem )
# # newList.append("ramkishor") #appends the list Item to the end
# print(listName)
# print(newList)

# list.extend(listName)
# print(list)

#we can concanate two lists
newList.extend(list)
print(newList)
# print(newList + list)