n = int(input("Enter n value:"))
for i in range (2,n+1):
    flag = 0
    for k in range(2,i-1):
        if(i%k==0):
            flag = 1
            break
    if(flag==0):
        print(i)    
