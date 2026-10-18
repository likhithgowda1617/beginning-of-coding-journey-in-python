n=int(input("enter the no to find the factorial of this number:"))
if n<0:
    print("factorial of negative number is not possible")
elif n==0 or n==1:
    print("the factorial of",n,"is 1")
else:
    fact=n
    for i in range(n,1,-1):
      
      fact=fact*(i-1)
      
    print("the factorial of",n,"is",fact)