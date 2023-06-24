print("welcome to the gas bill hill calculator")

account = int(input("Enter account num "))
month = int(input("Enter the month num "))

if month > 12 or month < 1:
    print("Wtf")
    



realElec = True
while realElec == True:

    ePlan = input("Enter your electercity plan:")

    if ePlan == "EFIR":
        realElec = True
    elif ePlan == "ELIR":
        realElec = True
    else:
        print("Unknown")
        realElec = False

print("Enter amount of elec used in month:" , month , "(in kwh)")
eUse = float(input())

if ePlan == "ELIR":
    elect = float(eUse * 0.911)
elif ePlan == "EFIR":
    if eUse > 1000:
        eRemain = eUse - 1000
        elect = ((1000*0.6363)+(eRemain * 0.6363))
    else:
        elect = float(eUse * 0.0636)

provinces_5 = ["AB","BC","MB","NT","NU","QC","SK","YT"]
provinces_15 = ["NB", "ML","NS","PE"]
provinces_13 = "ON"
province = input("Enter your abverriated province:")

if province in provinces_5:
    tax_rate = 0.05
if province in provinces_15:
    tax_rate = 0.15
if province in provinces_13:
    tax_rate = 0.13
total = (elect * tax_rate) +1.32 + 120.62


print(total)



