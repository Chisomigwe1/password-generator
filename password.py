
import random
a="abcdefghijklmnopqrstuvwxyz"
b="0123456789"
c="!@#$$%^&*"
string= a+b+c
lenght=5
password ="".join(random.sample(string,lenght))

print("new password:" +password)







