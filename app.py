import random

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lowercase = uppercase.lower()

numbers = "0123456789"

symbols = "~!@#$%^&*()_<>"

password = uppercase + lowercase + numbers+symbols

length = input("Enter the lenght of your password : ")

create = random.sample(password, int(length))

create_pass = ''.join(str(i) for i in create)

print(f"Your password is : {create_pass}")