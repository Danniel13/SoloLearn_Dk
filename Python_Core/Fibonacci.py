# num = 5


# def fibonacci(n):
# 	#complete the recursive function
#   x=range(1,n+1)
#   x=list(x)
#   for i in x:
#     print(i+i)
	


# fibonacci(num)
num = int(input())


def fibonacci(n):
  if n <= 1:
      return n
  else:
      return fibonacci(n-1) + fibonacci(n-2)
  

for i in range(num):
    print(fibonacci(i))