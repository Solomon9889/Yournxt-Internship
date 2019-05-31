input = str(input("Enter your string"))

flag =0
dec = 89
try:
    dec = int(input)
    flag = 1
except(ValueError):
    try:
        dec = float(input)
        flag = 2
    except(ValueError):
        print('false')
if(flag ==1 or flag == 2):
    print("True")


    
