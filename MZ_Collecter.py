import random
import string
s = input("Enter Path : ")

def getPassword(length):
    """Generate a random string"""
    str = string.ascii_lowercase
    return ''.join(random.choice(str) for i in range(length))
    
s1 = getPassword(8) 
s2 = s1 + '.exe'
def search(arr, x, y):
  
    for i in range(len(arr)):
  
        if arr[i] == x:
            if(arr[i+1] == y):
                return i
            else:
                continue
  
    return -1

f = open(s, 'r+b')
data = f.read()
l = len(data)
M_word = 77
Z_word = 90
result = search(data,M_word,Z_word)

data2 = data[result:l-1]
print(hex(data2[0]))
if result != -1:
    print("MZ present at :", result)
else:
    print("MZ not present")
 
with open(s2, 'wb') as f:
    f.write(data2)


 


