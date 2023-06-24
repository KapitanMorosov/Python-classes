List = [1 , 2 , 3 , 4 ]
print(List)

#adds item to the end of the list
List.append(5)
print(List)

#insert puts stuff at a desginated position. First value is the position and the second one is the number tiself
List.insert(0,1)
print(List)

#Count how much instances appears.
print(List.count(1))

#reverses the list
List.reverse()
print(List)


List.sort
print(List)

#removes first instance of item we call
List.remove(1)
print(List)

#SHows the legnth of the list
print(len(List))

#will remove an item at place that is given
List.pop(0)
print(List)

x = List.copy()
print(x)
List.append("GG")
print(List)

#appends a list to the end of an another list
y = [3,4]
List.extend(y)
print(List)

#clears the list
List.clear()
print(List)



