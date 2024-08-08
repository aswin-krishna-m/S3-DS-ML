def gcd(m,n):
    if m<n:
        m,n = n,m
    if m%n==0:
        return n
    else:
        return gcd(n,m%n)
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
print("GCD is : ", gcd(a,b))


"""
OUTPUT

Enter first number: 8
Enter second number: 6
GCD is :  2

"""
