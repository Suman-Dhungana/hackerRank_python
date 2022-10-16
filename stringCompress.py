from itertools import groupby

x = input()
compress=[]
for k,g in groupby(x):
    compress.append(len(list(g)))
    compress.append(k)
    print('(%s)' % ', '.join(map(str,compress)),end=" ")
    compress=[]