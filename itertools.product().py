A=input()
listA=A.split()
B=input()
listB=B.split()
ls=[]
row=[]
for x in listA:
    for y in listB:
        ls.append(x)
        ls.append(y)
        row= '(%s)'% ', '.join(map(str,ls))
        print(row, end=' ')
        ls=[]
