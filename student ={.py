student ={
    "registred": True,
    "age":31,
    "hairColour":["white","black","brown"]
}
print (student)
print (student["age"])
print(len(student))

#other way to create a dictonary
student = dict(name = "John", age = 13 , registred = True)
print(student)

student['city'] = 'calgary'
student.update({'gender':'m'})
print(student)

student.pop('city')
student.clear
print(student)


