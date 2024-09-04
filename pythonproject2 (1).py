import random
print('Welcome to your password')
def passwordgenerator():

 string="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()<>?"

 number=int(input("Number of passwords:"))
 length=int(input("your password length:"))

 print('\nhere are your passwords:')
 for  _  in range(number):
     passwords=''
     for _ in range(length):
         passwords += random.choice(string)
     print(passwords)
passwordgenerator()
