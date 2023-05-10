x = [6,3,9,2]
big = x[0]
small = x[0]
for i in range(1,len(x)):
    if x[i]>big:
        big = x[i]
    if x[i]<small:
        small = x[i]
print(f"the largest number is{big}")
print(f"the smallest number is{small}")