def fun(n):
    return lambda a:a*n
n=fun(3)
print(n(5))
