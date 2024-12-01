#3. Write a function to find the factorial of a number using recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:

        return n*factorial(n-1)
x= int(input("Entere non negative integer : "))
if x<1 :
    print ("Your number is Negative, Can't find factorial")
else:
    print("The Factorial of given number is ", factorial(x))