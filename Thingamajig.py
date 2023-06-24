List = [1,2,3]

print(List)


x = List.copy()
x.append("car") #adds to end  #this will mess up the sort code if ran together as sort() can't sort items that arent numbers
print(x)
print(List)


List.insert(0,3) #at position 0 put three
print(List)


print(List.count(3)) ##counts how many threes there are

List.reverse()#reverses list entities
print(List)

List.sort()
print(List) #sorts list  


List.remove(3) #removes first instance of '3' in list
print(List)

List.pop(0) #removes at specific position 
print(List)


y = [4,5]
List.extend(y)#adds to end 
print(List)


print(List.index(3)) #tells you position of where the first instance of '3' is 

print(len(List))#length 

print(List[1]) ##prints whatever variable is at pos 1 

List.clear()#clears all 


print(List) 
