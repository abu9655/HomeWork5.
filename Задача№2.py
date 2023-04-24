def num (a,sum):
    if a -1!=0:   
        sum = sum * a
        a -= 1  
    else:
        print(sum)
        return 
    num (a,sum)
def num1 (a,sum):
    if a !=0:   
        sum = sum + a
        a -= 1
    else:
        print(sum) 
        return 
    num1 (a,sum)

a=int(input())
sum = int(1)
num (a,sum)
num1 (a,(sum-1))