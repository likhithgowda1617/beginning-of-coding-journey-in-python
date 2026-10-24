#clever if operator
#syntax:<var>=(false_value,true_value)[<condition>]
sal=float(input("enter the salary :"))
tax=sal*(0.1,0.2)[sal>=50000]
print("the tax amount is:",tax)