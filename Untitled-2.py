x = "test"
try:                            # tries to execute a code that follows it
    print(x) 
except NameError:               #throws error whenever there is a problem with name
    print("Wrong name") 
except:                         #throws exception whenever there is any error
    print("error")
else:                           #executes when there is no erros in try block
    print("No error")
finally:                        #executes after try block no matter why
    print("Try-exepction finished")

y=0
print(y)

if y < 1:
    raise Exception("y cannot be < 1") #if conditions is sastisfied, throws exception, and stops program execution
print(x)