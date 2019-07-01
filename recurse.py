import sys
input=int(sys.argv[1])
sys.setrecursionlimit(3000)

def fact(n):
  if n == 0:
    return 1
  else:
    return n * fact(n-1)

print(fact(input))

