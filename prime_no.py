n=int(input("enter the no to be checked"))
flag=0
if n>1:
    for i in range(2,int(n/2)+1):
        if n%i==0:
            flag=1
            break
    if flag==1:
        print(n,"is not a prime no")
    else:
        print(n,"is a prime no")
else:
    print("prime no are always>1")