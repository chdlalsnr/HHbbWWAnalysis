import math 

def rebin(edges1,cont1,err1,edges2):
    assert len(cont1) == len(edges1)-1
    assert len(err1) == len(edges1)-1
    verbose = True
    cont2 = [0.]*(len(edges2)-1)
    err2 = [0.]*(len(edges2)-1)
    i1 = 0
    i2 = 0
    if verbose:
        print ('='*30)
        print ('Rebin')
    while (i1 < len(edges1)-1 and i2 < len(edges2)-1):
        if verbose:
            print ('-'*20)
            print ('Looking at bin i1 %d/%d edges = [%.3f,%.3f] -> %.5f (cont), %.5f (err squared), compared to bin i2 %d/%d edges = [%.3f,%.3f] -> %.5f (cont), %.5f (err squared)'
                        %(i1,
                          len(edges1)-1,
                          edges1[i1],
                          edges1[i1+1],
                          cont1[i1],
                          err1[i1]**2,
                          i2,
                          len(edges2)-1,
                          edges2[i2],
                          edges2[i2+1],
                          cont2[i2],
                          err2[i2]**2))
        if edges1[i1+1] <= edges2[i2+1]: 
            if verbose:
                print ('edges1 <= edges2 : adding %.5f (cont) and %.5f (err squared) to i2 %d edges = [%.3f,%.3f]'%(cont1[i1],err1[i1]**2,i2,edges2[i2],edges2[i2+1]))
            cont2[i2] += cont1[i1]
            err2[i2] += err1[i1]**2
        else:
            pr = cont1[i1]
            sve = edges1[i1]
            si2 = i2
            cont_frac = []
            nums = []
            while edges1[i1+1] >= edges2[i2+1] and i2 < len(edges2)-2:
                pl = (edges2[i2+1]-sve)/(edges1[i1+1]-sve) * pr
                nums.append(edges2[i2+1]-sve)
                sve = edges2[i2+1]
                pr -= pl
                assert pl >= 0
                assert pr >= 0
                cont_frac.append(pl)
                i2 += 1
            cont_frac.append(pr)
            nums.append((edges1[i1+1]-edges1[i1])-sum(nums))
            for cf,num in zip(cont_frac,nums):
                cont2[si2] += cf
                add_err = num**2/sum([n**2 for n in nums]) * err1[i1]**2
                err2[si2] += add_err
                if verbose:
                    print ('edges1 > edges2 : adding %.5f (cont) and %.5f (err squared) to i2 %d edges = [%.3f,%.3f]'%(cf,add_err,si2,edges2[si2],edges2[si2+1]))
                si2 += 1
        i1 += 1
    assert abs(sum(cont1)-sum(cont2))<1e-9
    assert abs(sum([e**2 for e in err1])-sum(err2))<1e-9
    err2 = [math.sqrt(e) for e in err2]
    return edges2,cont2,err2

edges1 = [0,0.3,0.35,0.5,1.]
edges2 = [0,0.2,0.4,0.6,0.8,1.]
cont1 = [0.1,0.2,0.3,0.4]
err1 = [c/2 for c in cont1]
print ('edges 1',edges1)
print ('edges 2',edges2)
print ('content 1',cont1)
print ('error 1',err1)
edges2,cont2,err2 = rebin(edges1,cont1,err1,edges2)
print ('edges 1',edges1)
print ('edges 2',edges2)
print ('content 1',cont1)
print ('content 2',cont2)
print ('error 1',err1)
print ('error 2',err2)

