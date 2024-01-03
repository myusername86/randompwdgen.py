import random

print("hello! welcome to random password generation")

no_of_pawd=int(input("how many passwords do you want?"))

lenofpwd=int(input("what is length of your password?"))

a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"

for x in range(no_of_pawd):

    pwd=""

    for y in range(lenofpwd):

        pwd=pwd + random.choice(a)

    print(pwd)