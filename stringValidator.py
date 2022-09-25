s = input()
rows=[]
column=[]
for y in s:
    a=y.isalnum()
    column.append(a)
rows.append(column)
column=[]
for y in s:
    a=y.isalpha()
    column.append(a)
rows.append(column)
column=[]
for y in s:
    a=y.isdigit()
    column.append(a)
rows.append(column)
column=[]
for y in s:
    a=y.islower()
    column.append(a)
rows.append(column)
column=[]
for y in s:
    a=y.isupper()
    column.append(a)
rows.append(column)
column=[]
for row in rows:
    if True in row:
        print(True)
    else:
        print(False)