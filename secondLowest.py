#Find the 2nd Lowest Score and print Name from the list
listl= []
smallest = small = float('inf')
for x in range(int(input(f"Enter Total Number of Records: "))):
    name = input(f"Enter Name for record {x+1}: ")
    score = float(input("Enter the Score: "))
    li = [name,score]
    listl.append(li)
for n,i in listl:
    if i<smallest:
        small = smallest
        smallest=i
    elif i < small and i != smallest:
        small = i
listl.sort()
print("Entries with 2nd Lowest Score: ")
for n,i in listl:        
    if i == small:
        print(n)