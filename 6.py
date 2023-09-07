nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")

else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
     
       n1 = n2
       n2 = nth
       count+= 1  
//How many terms? 7
Fibonacci sequence:
0
1
1
2
3
5
8
> //



def fibonacciSeries(i):
    if i <= 1:
        return i
    else:
        return (fibonacciSeries(i - 1) + fibonacciSeries(i - 2))

num = int(input("Enter the number upto which series should be printed: "))
if num <= 0:
    print("Please enter a positive number")
else:
    print("Fibonacci Series:", end=" ")
    for i in range(num):
        if i < num - 1:
            print(fibonacciSeries(i), end=", ")  
        else:
            print(fibonacciSeries(i))  
          //Enter the number upto which series should be printed: 7
Fibonacci Series: 0, 1, 1, 2, 3, 5, 8//
