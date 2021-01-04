#code to print Fibonacci series untill 'n' value
n = int(input("Enter the number of terms in the series, n: "))
a = 0
b = 1
x = 0
y = 1
print("Fibonacci Series till nth term: ", end = " ")

for y in range (n):
  print(x, end = " ")
  y += 1
  a = b
  b = x
  x = a + b
