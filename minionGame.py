def countSubString(string,listl):
    counter=0
    for y in listl:
        for x in range(len(string)):
            liLen= len(y)
            if y in string[x:x+liLen] and len(string[x:x+liLen])==liLen:
                counter+=1
    return counter

def minion_game(string):
    # your code goes here
    vList = ['A','E','I','O','U']
    lis=[]
    lik=[]
    for x,y in enumerate(string):
        for i in range(len(string)):
            strg= string[x:i+1]
            if strg!="":
                if y not in vList:  
                    lis.append(strg)
                else:
                    lik.append(strg)
    score_St=countSubString(string,set(lis))
    score_Ke=countSubString(string,set(lik))
    if score_St>score_Ke:
        print(f"Stuart {score_St}")
    elif score_Ke>score_St:
        print(f"Kevin {score_Ke}")
    else:
        print("Draw")
s = input()
minion_game(s)
