t=int(input())
for a0 in range(t):
    y =int(input())
    y-=1
    n=y//3
    n2=y//5
    n3=y//15
    s=(n*(n+ 1)//2)*3
    s2=(n2*(n2+1)//2)*5
    s3=(n3*(n3+1)//2)*15
    print(s+s2-s3)
