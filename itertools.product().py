A=input().split()
B=input().split()
ls=[]
for x in A:
    for y in B:
        ls.append(x)
        ls.append(y)
        row= '(%s)'% ', '.join(map(str,ls))
        print(row, end=' ')
        ls=[]
