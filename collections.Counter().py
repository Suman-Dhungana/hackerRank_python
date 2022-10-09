#Find total earned by seller selling the shoes which are in stock

from collections import Counter
noShoes=int(input("Enter the total number of shoes in stock:"))
ls=[None] * noShoes
shoSize=input("Enter all the shoes size available:").split()
try:
    for i in range(noShoes):
        ls[i]=shoSize[i]
except IndexError: 
    print(f'Number of Shoes given is lower than that in Stock ({noShoes} != {len(shoSize)}).')
shoeDict = Counter(ls)
ls=[]
cust=int(input("Enter the number of Customers:"))
print(f"Enter shoe size and price for all {cust} customer offers:")
for x in range(cust):
    custOff=input().split()
    ls.append(custOff)
sum=0
for x in ls:
    val=Counter(shoeDict).get(x[0])
    if x[0] in shoeDict.keys() and val> 0:
        val-=1
        shoeDict[x[0]] = val
        sum=sum+int(x[1])
print(f"Total Earned is {sum}")