#Practice 5 Recursion
#6/10/24
#Owen O'Neil


# 1

#a. if n == 0, return 1

#b. if n! = n (n-1)

#c. factorial(n) = 1                  if n = 0
#                  n * factorial(n-1) if n > 0

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# 2

#a. if n == 0, return 0
#   if n == 1, return 1 

#b. fibonacci(n-1) +fibonacci(n-2)

#c. fibonacci(n) = 0                               if n=0
#                  1                               if n=1
#                  fibonacci(n-1) + fibonacci(n-1) if n>1

def fibbonaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibbonacci(n - 2)

# 3

#a. if len(s) == 0, return the string
    
#b. string(s[1:]) + s[0]

#c. string(s) = s                    if len(s)=0
#               string(s[1:]) + s[0] if len(s) > 0


def string(s):
    if len(s) == 0:
        return s
    else:
        return string(s[1:]) + s[0]

# 4

#a. if n == 0 return 0

#b. n%10 + Numsum(n // 10)

#c. Numsum(n) = 0                   if n=0
#            n%10 + Numsum(n // 10) if n>0

def Numsum(n):
    if n == 0:
        return 0
    else:
        return n%10 + Numsum(n//10)

# 5

#a. if len(array) == 0, return [[]]

#b.  MutatedArray = []
#        for i in range(len(array)):
#            for m in MutatedArray(array[:i] + array[i+1:]):
#                MutatedArray.append(array[[i]] + m)
#        return MutatedArray

#c. posibilities(array) = [[]]                      if len(lst)=0
#                         for i in range(len(lst)): for m in MutatedArray(lst[:i]+lst[i+1:]):
#                         [lst[i]]+p                append [lst[i]] in front of each m
​ 

def posibilites(array):
    if len(array) == 0:
        return  [[]]
    else:
        MutatedArray = []
        for i in range(len(array)):
            for m in MutatedArray(array[:i] + array[i+1:]):
                MutatedArray.append(array[[i]] + m)
        return MutatedArray
     
# 6

#a. if n = 0 return 0
#   if n = 1 return 1
#   if n = 2 return 2
#   if n = 3 return 3

#b. series(n) = series(n-1) + series(n-2) + series(n-3) 
    

#c. series(n) = 0                       if n=0
#               1                       if n=1
#               2                       if n=2
#               3                       if n=3
#               a(n−1)+a(n−2)+a(n−3)    if n≥4


def series(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    else:
        return series(n-1) + series(n-2) series(n-3)
    
    
    
        
​
 



