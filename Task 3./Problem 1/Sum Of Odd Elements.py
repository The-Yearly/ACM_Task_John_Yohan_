x=int(input("Enter The Number Of Elements In List "))
l=[]
if x>0 and x<101:
    for g in range(x):
        y=int(input("Enter The Number "))
        l.append(y)
    s=0
    for j in l:
        if j%2==1:
            s+=j
    print(s)
else:
    print("Pls Enter A Number Between 1-100")
