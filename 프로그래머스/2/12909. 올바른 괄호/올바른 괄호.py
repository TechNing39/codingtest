def solution(s):
    open_count=0
    if s[0]==')' or s[-1]=='(':
        return False
    for x in s:
        if x=='(':
            open_count+=1
        else:
            open_count-=1
        
        if open_count<0:
            return False
            
        
        

    return open_count==0