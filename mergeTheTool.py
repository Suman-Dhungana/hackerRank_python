def merge_the_tools(string, k):
    temp=[]
    for i in range(0,len(string),k):
        sub=string[i:i+k]
        for x in sub:
            if x not in temp:
                temp.append(x)
                stn=''.join(temp)
        temp=[]
        print(stn)

string, k = input(), int(input())
merge_the_tools(string, k)