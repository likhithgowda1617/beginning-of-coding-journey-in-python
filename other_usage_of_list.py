# a=input("enter the string:")







# syntax:
#map(functionname, iterable)
# a=list(map(int,input("enter the numbers:").split()))
# print(a)


#list comprehension
# a=[str(x**3) for x in range(10)]
# print(a)
a=[[(x**2),(x**3),(x**4)] for x in range(10) if x%2==0]
print(a)

