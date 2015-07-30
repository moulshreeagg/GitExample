def recur_fib(n):
   if n <= 1:
       return n
   else:
       return(recur_fib(n-1) + recur_fib(n-2))

def main ():
  nterms = int(input("How many terms? "))

  if nterms <= 0:
     print("Plese enter a positive integer")
  else:
     print("Fibonacci sequence:")
     for i in range(nterms):
         print(recur_fib(i))

if __name__ == '__main__':
      main()