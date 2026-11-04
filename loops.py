# word="Hello everyone" 
# for i in word:
#     print(i,end=" ")

a=list()
n=3

for i in range(n):
    ele=int(input("enter the number: "))
    a.append(ele)
print(a)
for i in range(len(a)):
    print(a[i],end="\t")