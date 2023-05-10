
from functools import reduce
x=lambda a,b:a+b
p=reduce(x,[1,2])
print(p)