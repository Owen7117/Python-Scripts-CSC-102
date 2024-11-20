#Recursion Revisited
#6/7/24

#Recurrence relation is an queation that recursively defines a sequence

def f(x):
    if x == 0:
        return 1
    else:
        return x * f(x-1)
   
----------------------------------------


def s(x):
    y=60000
    x=0
    if x == 40:
        return y
    else:
        return (y == y *.03) s(x+1)

print(s)