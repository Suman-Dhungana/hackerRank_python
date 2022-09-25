def binary(x):
    dSum=''
    while(x>0):
        dRem= str(x%2)
        dSum= dRem+dSum
        x= int(x/2)
    return dSum

def octa(x):
    oSum =''
    while(x>0):
        oRem = str(x%8)
        oSum = oRem + oSum
        x = int(x/8)
    return oSum

def hexa(x):
    dLs=['10','11','12','13','14','15']
    hLs=['A','B','C','D','E','F']
    hSum=''
    while(x>0):
        hRem = str(x % 16)
        for i in range(len(dLs)):
            if hRem == dLs[i]:
                hRem= hLs[i]
        hSum = hRem + hSum
        x=int(x/16)
    return hSum



def print_formatted(number):
    lgt= len(str(binary(number)))
    for x in range(1,number+1):
        dec=str(x)
        bin_con=str(binary(x))
        octa_con=str(octa(x))
        hexa_con=str(hexa(x))
        print(dec.rjust(lgt)+' '+octa_con.rjust(lgt)+' '+hexa_con.rjust(lgt)+' '+bin_con.rjust(lgt))
        


n = int(input())
print_formatted(n)