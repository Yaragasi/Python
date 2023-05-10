str="python pro"
sub="pro"
flag=False
pos=-1
while True:
    pos=str.find(sub)
    if pos==-1:
        break
    print("Found at", pos+1)
    flag=True
    if flag==False:
        print("not found")