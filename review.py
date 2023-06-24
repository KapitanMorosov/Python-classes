x = "poopy"
try:
    print(x + 3)
except NameError:
    print("farted")
except TypeError:
    print("Ripped")
else:
    print("Works")
finally:
    print("print(print(Print))")