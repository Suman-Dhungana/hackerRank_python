from itertools import groupby

x = input()
keyLen=[]
for k,g in groupby(x):
    keyLen.append(len(list(g)))
    keyLen.append(k)
    print('(%s)' % ', '.join(map(str,keyLen)),end=" ")
    keyLen=[]