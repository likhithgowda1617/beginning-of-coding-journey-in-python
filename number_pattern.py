n=int(input("enter the number to generate it s pattern:"))
for i in range(n+1):
    j=1
    while j<=i:
        print(j,end=" ")
        j=j+1
    
    print()