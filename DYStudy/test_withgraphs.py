import ROOT

f = ROOT.TFile("test.root")
cdf1 = f.Get("cdf1")
cdf2 = f.Get("cdf2")
cdf3 = f.Get("cdf3")

g1 = ROOT.TGraph(cdf1.GetNbinsX()+1)
g2 = ROOT.TGraph(cdf2.GetNbinsX()+1)
g3 = ROOT.TGraph(cdf3.GetNbinsX()+1)
ginv1 = ROOT.TGraph(cdf1.GetNbinsX()+1)
ginv2 = ROOT.TGraph(cdf2.GetNbinsX()+1)

for i in range(0,cdf1.GetNbinsX()+1):
    g1.SetPoint(i,cdf1.GetXaxis().GetBinUpEdge(i),cdf1.GetBinContent(i))
    ginv1.SetPoint(i,cdf1.GetBinContent(i),cdf1.GetXaxis().GetBinUpEdge(i))
for i in range(0,cdf2.GetNbinsX()+1):
    g2.SetPoint(i,cdf2.GetXaxis().GetBinUpEdge(i),cdf2.GetBinContent(i))
    ginv2.SetPoint(i,cdf2.GetBinContent(i),cdf2.GetXaxis().GetBinUpEdge(i))
for i in range(0,cdf3.GetNbinsX()+1):
    g3.SetPoint(i,cdf3.GetXaxis().GetBinUpEdge(i),cdf3.GetBinContent(i))

from CDFShift import CDFShift

getArray = CDFShift.getArray
e1,c1 = getArray(cdf1)
e2,c2 = getArray(cdf2)
e3,c3 = getArray(cdf3)

c12 = sorted(list(set(c for c in c1+c2)))

def getSlope(e,c):
    m = []
    for i in range(len(c)):
        yup = c[i]
        ylow = c[i-1] if i>0 else 0
        xup = e[i+1]
        xlow = e[i]
        m.append((yup-ylow)/(xup-xlow))
    return m

def splitSlope(e,c,m,nc):
    assert all([ic in nc for ic in c])
    idx = 0
    nm = []
    ne = []
    for i in range(len(nc)):
        if nc[i] > c[idx]:
            idx += 1
        nm.append(m[idx])
    return nm

def makeDelta(e1,e2,m12,c1,c2,c12):
    return delta   

            
    

m1t = getSlope(e1,c1)
m2t = getSlope(e2,c2)

m1 = splitSlope(e1,c1,m1t,c12)
m2 = splitSlope(e2,c2,m2t,c12)

m12 = [(mi1-mi2)/(mi1*mi2) if mi1!=0 and mi2!=0 else 0. for mi1,mi2 in zip(m1,m2)]

i1 = 0
i2 = 0
delta = []
while c1[i1] <= 0:
    i1 += 1
while c2[i2] <= 0:
    i2 += 1
for i in range(len(c12)):
    if c12[i]>c1[i1]:
        i1+=1
    if c12[i]>c2[i2]:
        i2+=1
    print ('----------')
    print ('i',i,c12[i],m12[i])
    print ('i1',i1,len(c1),c1[i1],e1[i1])
    print ('i2',i2,len(c2),c2[i2],e2[i2])
    y = c12[i]
    y0 = c12[i-1] if i>0 else 0
    x1 = e1[i1]
    x2 = e2[i2]
    delta.append((e2[i2]-e1[i1])+m12[i]*(y-y0))

i1 = 0
i2 = 0
delta2 = []
nc3 = []
while c1[i1] <= 0:
    i1 += 1
while c2[i2] <= 0:
    i2 += 1
for i3 in range(len(c3)):
    y = c3[i3]
    if y <= 0.:
        continue
    while c3[i3] > c1[i1]:
        i1 += 1
    while c3[i3] > c2[i2]:
        i2 += 1
    y10 = c1[i1-1]
    y20 = c2[i2-1]
    x10 = e1[i1]
    x20 = e2[i2]
    x1 = x10 + (1/m1[i1])*(y-y10)
    x2 = x20 + (1/m2[i2])*(y-y20)
    delta2.append(x2-x1)
    nc3.append(c3[i3])
    assert y>=y10
    assert y>=y20
    assert y<=c1[i1]
    assert y<=c2[i2]


g = ROOT.TGraph(len(c12))
g_inv = ROOT.TGraph(len(c12))
delta3 = []
for i in range(len(c12)):
    x1 = ginv1.Eval(c12[i])
    x2 = ginv2.Eval(c12[i])
    print (x2-x1,delta[i],c12[i])
    g.SetPoint(i,x2-x1,c12[i])
    g_inv.SetPoint(i,c12[i],x2-x1)
    delta3.append(x2-x1)


ng3 = ROOT.TGraph(cdf3.GetNbinsX())
for i in range(cdf3.GetNbinsX()):
    #y = cdf3.GetBinContent(i)
    #d = g_inv.Eval(y)
    #ng3.SetPoint(i,cdf3.GetBinLowEdge(i)+d,y)
    ng3.SetPoint(i,cdf3.GetBinLowEdge(i)+d,y)

import IPython
IPython.embed()
