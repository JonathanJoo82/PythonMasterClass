name = input("what is your name?")
age = int(input("how old are you {0}?".format(name)))

if age >= 18:
    print("you are able to vote")
else:
    print("you are not old enough to vote")

number = int(input("Please enter a number."))

if number >= 80:
    print("the number is equal or greater than 80")
elif 80 > number >= 60:
    print("the number is less than 80 but greater or equal to 60.")
else:
    print("number is less than 60")


str = "this is a test string!"
num = 10

if num > 5 and str == "this is a test string":
    print("num is greater then 5")
elif num == 10 and str != "this is a test string":
    print("number is match but not string")
else:
    print("nothing matched")