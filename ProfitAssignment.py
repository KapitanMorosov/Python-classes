#Instructions:
#Calculate total profit of the day in CDN$:

#Ask the user to indicate a product a category(1-5) then indicate the quanity sold in that category
#Ask the user to enter the category and quanity up to five times(for the days when there are sales in all five categories)
#Allow the user to stop entering data if there arent sales in all five categories by entering zero for the product category
#Return an error message when the users the user enters value other than 0,1,2,3,4,5 for the product category.




ApplePhone = 120.45
AndroidPhone = 99.50
AndroidTablet = 86.73
WindowsTablet = 81.45
AppleTablet = 75.99

#Might be unnecessary
Cat1 = ApplePhone
Cat2 = AndroidPhone
Cat3 = AndroidTablet
Cat4 = WindowsTablet
Cat5 = AppleTablet

List1 = [1 , 2 , 3 , 4 , 5]

print("Welcome to the profit calculator")

Ask1 =  int(input("Select  the  category"))
if Ask1 == 1:
    Ask1 = Cat1
    print(Ask1)
    AskQ = int(input("Enter the quantity sold "))

if Ask1 == 2:
    Ask1 = Cat2
    print(Ask1)
    AskQ = int(input("Enter the quantity sold "))

if Ask1 == 3:
    Ask1 = Cat3
    print(Ask1)
    AskQ = int(input("Enter the quanity sold "))

if Ask1 == 4:
    Ask1 = Cat4
    print(Ask1)
    AskQ = int(input("Enter the quantity sold "))

if Ask1 == 5:
    Ask1 = Cat5
    print(Ask1)
    AskQ = int(input("Enter the quantity sold "))









    






