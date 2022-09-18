n = int(input("Total Numbers: "))
arr = map(int, input(f"Enter {n} numbers: ").split())
listl= list(arr)
maximum = runner_up = None
for num in listl:
    if not maximum or num > maximum :
        runner_up = maximum
        maximum = num
    elif not runner_up or num < maximum and num > runner_up:
        runner_up = num
print(runner_up)