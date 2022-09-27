def solve(s):
    lsl=[]
    ls=s.split(" ")
    for x in ls:
        if x.isalpha():
            x=x[0].upper()+x[1:]
        lsl.append(x)
    return " ".join(lsl)

s = input()
result = solve(s)
print(result)