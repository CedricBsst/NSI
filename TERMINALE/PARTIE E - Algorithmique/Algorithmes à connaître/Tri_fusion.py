def tri(l):
    if len(l) > 1:
        
        i_millieu = len(l)//2
        l1 =l[0:i_millieu]
        l2 =l[i_millieu:]
        l1 =tri(l1)
        l2 =tri(l2)
        return fusion(l1,l2)
    
    else:
        return l 
    
        
def fusion(l1,l2):
    if len(l2) == 0:
        return l1
    elif len(l1) == 0:
        return l2
    elif l1[0] < l2[0]:
        return [l1[0]] + fusion(l1[1:],l2)
    else:
        return [l2[0]] + fusion(l2[1:],l1)
    