# myString = input("enter the string :   ")
# vowels = ['a', 'i', 'u', 'o', 'e']
# count = 0
# for i in myString:
#     for v in vowels:
#         if v == i:
#             count += 1

# print (f"the count of vowels is : {count}")


#####################################################

# string = input("enter mumber :  ")
# if string.isdigit():
#     num = int(string)
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 5 == 0:
#         print("Buzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     else:
#         print("not Fizz or Buzz")
# else:
#     print("enter valid number")


################################################
# #####   1
# mystring = input("Enter your string : ")
# print(mystring[::-1])
# #####  2
# print(input("Enter your string : ")[::-1])

###############################################

# string = input("enter mumber :  ")
# if string.isdigit():
#     r = float(string)
#     by = 3.14
#     area = by * (r**2)
#     circumference = by*r*2
#     print(f"The area is : {area}")
#     print(f"The circumference is : {circumference:.3g}")

# else:
#     print("enter valid number")
##############################################
# import re
# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# name = input("enter your name :  ")
# if name.isalpha():
#     email = input("enter your email :  ")
#     if(re.fullmatch(regex, email)):
#         print("Valid Email")

#     else:
#         print("Invalid Email")
# else:
#     print("enter valid name")

#################################################
# string="prints the number of times the string 'iti' occurs in"

# print(string.count("iti"))