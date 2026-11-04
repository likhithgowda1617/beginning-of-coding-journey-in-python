def basic_calculator(n1,n2):
    if operator=='+':
        return n1+n2
    elif operator=='-':
        if n1>n2:
            return n1-n2
        else:
            return n2-n1
    elif operator=='*':
        return n1*n2
    elif operator=='/':
        if n2==0:
            return "Denominator can't be zero"
        else:
            return n1/n2
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
operator=input("Enter the operator(+,-,*,/):")
print(basic_calculator(n1,n2))
