input = int(input("Enter the number"))

def rev(num): 
    return num[::-1] 

def palfnc(num):
    reverse = rev(str(num))
   
    if(reverse == str(num)):
        return True
    else:
        return False


i = 1
while(True):
    right = input+i
    left = input-i
    a = palfnc(right)
    b = palfnc(left)
    if(a == True or b == True):
        break
    i = i+1
    
if(b== True):
    print(str(left))
else:
    print(str(right))

    


