import string   
import getpass 
import random # define the random module  
S = 3  # number of characters in the string.  
# call random.choices() string module to find the string in Uppercase + numeric data.  
extra = ''.join(random.choices(string.ascii_lowercase + string.digits, k = S))    
extra1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S)) 
extra2= ''.join(random.choices(string.ascii_lowercase + string.digits, k = S)) 
secret = getpass.getpass("enter your secret code ")

list1 = []
for letter in secret:
    list1.append(letter)
    
# list1.sort(reverse=True)
n = len(list1)
mid = int(n/2)
if(n > 2):
    list1.append(list1[0])
    list1.remove(list1[0])
    list1.insert(mid , extra1)
    # list1.insert(mid+2 , extra)
    a = list1.pop(n-2)
    list1.insert(0 , a)
    list1.insert(0 , extra)
    list1.append(extra2)  
else:
    list1.sort(reverse=False)
    list1.insert(0 , extra)
    list1.append(extra)    

str1 = ""
for item in list1:
        str1 += item
print("your encoded message is = " , str1)

if(n > 2):
     list1.pop()
     list1.remove(list1[0])
     list1.remove(list1[mid+1])
     a = list1.pop()
     list1.insert(0 , a)
     b = list1.pop(1)
     list1.insert(n-2 , b)
else:
     list1.pop()
     list1.remove(list1[0])
     list1.sort(reverse=True)

str1 = ""
for item in list1:
        str1 += item

x = input("enter 'y' to decode the message ")
if(x == 'y'):
    print("your decoded message is = " , str1)
else:
     raise ValueError("invalid input")
