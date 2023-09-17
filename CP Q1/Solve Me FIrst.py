
def solveMeFirst(a,b):
	# Hint: Type return a+b below
    if a>0 and a<1001 and b>0 and b<1001:
        s=a+b
        return(s)
    else:
        print("Input is Out Of Constraits")
        return(None)

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)
