#count the no. of same string and print for ex wwwwrrrig will be w4r3ig
def countnsay(s):
    n = len(s)
    say = ""
    cur = ""
    count = 1
    for i in range(n-1):
        curr = s[i]
        nxt = s[i+1]
        if curr == nxt:
            count +=1
        elif(count>1):
            cur+=curr
            say+=(str(curr)+str(count))
            count = 1
        else:
            cur+=curr
            say+=str(curr)    
    cur += curr
    say+=(str(s[n-1])+str(count))
    print(cur) 
    print(say)

s = "wwwwaaadexxxxxx"
countnsay(s)