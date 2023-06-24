import string
import random

#store all characters in list
lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
digits= list(string.digits)
special_characters = list(string.punctuation)

good = False
while good == False:
    try:
        character_number = int(user_input)

        if character_number < 8:
            print("Your number should be atleast 8")
            user_input = input("please enter your number again: ")
        else:
            good = True
    except:
        print("please enter numbers only")
        user_input = input("How many characters do you want in your password: ")

random.shuffle(lowercase)
random.shuffle(uppercase)
random.shuffle(digits)
random.shuffle(special_characters)


all_characters = lowercase + uppercase + digits + special_characters
random.shuffle(all_characters)

password = ''.join(random.sample(all_characters, character_number) )
print("Your password is" , password)