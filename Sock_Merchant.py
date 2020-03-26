#Sock Merchant


def sockMerchant(n, ar):
    uq=[]
    for i in ar:
        if i not in uq:
            uq.append(i)
    print(uq)
    ans=0
    for x in uq:
        # print(x)
        p=x
        co=ar.count(p)
        # print(co)        
        if co>=2:
            ans+=(co//2)            
    return ans

