def fusion(l1, l2):
    if len(l1) == 0:
        return l2
    if len(l2) == 0:
        return l1
    if l1[0] <= l2[0]:
        return [l1[0]] + fusion(l2, [l1[i] for i in range(1,len(l1))])
    if l1[0] > l2[0]:
        return [l2[0]] + fusion(l1, [l2[i] for i in range(1,len(l2))])
    
def tri_fusion(l):
    if len(l) == 1:
        return l
    else:
        l1 = [l[i] for i in range(0, len(l)//2)]
        l2 = [l[i] for i in range(len(l)//2, len(l))]
        return fusion(tri_fusion(l1), tri_fusion(l2))
    