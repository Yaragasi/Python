def fun(a,b,c):
    yield a
    yield b
    yield c
    print("prasanthi")
print(fun(6,8,10))
for value in fun(2,3,4):
        print(value)
