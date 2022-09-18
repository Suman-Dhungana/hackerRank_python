n = int(input("Total Numbers: "))
arr = map(int, input(f"Enter {n} numbers: ").split())
listl= list(arr)
listl.sort()
maximum = runner_up = None
for num in listl:
    if not maximum or num > maximum :
        runner_up = maximum
        maximum = num
print(f"Runner Up is {runner_up}.")