AccountNum = input("Account Number: ")
AccountNum = int(AccountNum)
AmountGJ = input("Amount of GJ used: ")
AmountGJ = int(AmountGJ)
AmountKWH = input("Amount of electricty used: ")
AmountKWH = int(AmountKWH)
Month = input("Month: ")
Month = int(Month)



TypeE = input("Electricty plan: ")
TypeG = input("Gas plan: ")
Province = input("Province, enter the abbreviated version ex: (AB for Alberta): ")

list1 = ["AB","BC","MB","NT","NU","QC","SK","YK"]
list2 = ["NB","NL","NS","PE"]

monthlyF = 120.62
tax = 0 

if Province == list1:
    tax = 0.05
    print(tax)

if Province == list2:
    tax = 0.15
    print(tax)   

if Province == "ON":
    tax = 0.13
    print(tax)

