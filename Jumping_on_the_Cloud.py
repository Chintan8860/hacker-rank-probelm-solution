#Jumping on the Clouds

def jumpingOnClouds(c,n):
    ans = 0         #number of jumps
    i = 0           #position
    while i < n - 1:    #total clouds
        if i+1 == n:   
            i+=1
        elif c[i+2]==0:   #ignor thunderheads clouds
            i+=2
        else:           
            i+=1
        ans+=1
    return ans       
