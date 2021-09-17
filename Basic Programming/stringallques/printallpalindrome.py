def ispalindrome(ss):
    i = 0
    j = len(ss)-1
    while i<=j:
        ch1 = ss[i]
        ch2 = ss[j]
        if(ch1 != ch2):
            return False
        else:
            i+=1
            j-=1
    return True            


n = "abcc"
for i in range(0,len(n)):
    for j in range(i+1,len(n)):
        ss = n[i:j]
        if(ispalindrome(ss)==True):
            print(ss)
