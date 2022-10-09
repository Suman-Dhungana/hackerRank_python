A=input()
listA=list(A.split())
B=input()
listB=list(B.split())
ls=[]
row=[]
for x in listA:
    for y in listB:
        ls.append(x)
        ls.append(y)
        row.append(ls)
        ls=[]
    tup=tuple(row)
tup='%s' % ', '.join(map(str,tup))
# print(tup,sep=' ')
print(''.join(tup))