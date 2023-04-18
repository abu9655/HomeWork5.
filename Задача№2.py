import numpy as np
str1= np.random.randint(0,9,10)
print(str1)
x=0
a=0
sum=int(0)
for i in range(3):
    for j in range(len(str1)):
        if x < str1[j]:
            x=str1[j]
            a=j
    sum+=str1[a]
    str1[a]=0
    x=0
print(sum)          
