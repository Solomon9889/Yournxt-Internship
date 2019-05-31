

input = str(input("Enter your string")+" $")
block = ""
fblock = ""
flag1 = 0
i = 0
while(input[i]!= "$"):
        if(input[i]==" " and flag1 == 0):
                i= i+1
        else:
                flag1 = 1
                if(input[i] != " "):
                        
                        block = block + input[i]
                        
                else:
                        
                        fblock = block + " " + fblock
                        block = ""
                        flag1 = 0
                i = i+1
print("Output:" + fblock)       
        
        

