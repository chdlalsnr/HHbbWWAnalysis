import os
import sys
import ROOT

from CDFShift import CDFShift

#ROOT.gROOT.SetBatch(True)

f = ROOT.TFile('test.root')

h1 = f.Get('h1')
h2 = f.Get('h2')
h3 = f.Get('h3')

instance = CDFShift(h1,h2,h3)
instance.getShiftFromBinning()
instance.applyShift()

cdf1 = instance.cdf1
cdf2 = instance.cdf2
cdf3 = instance.cdf3
ncdf3 = instance.ncdf3
nh3 = instance.nh3
cdf3.Draw("hist same")

h1.SetLineColor(ROOT.kRed)
h2.SetLineColor(ROOT.kBlue)
h3.SetLineColor(ROOT.kGreen)
nh3.SetLineColor(ROOT.kMagenta)

cdf1.SetLineColor(ROOT.kRed)
cdf2.SetLineColor(ROOT.kBlue)
cdf3.SetLineColor(ROOT.kGreen)
ncdf3.SetLineColor(ROOT.kMagenta)

leg1 = ROOT.TLegend(0.6,0.6,0.9,0.9)
leg1.AddEntry(h1,'h1')
leg1.AddEntry(h2,'h2')
leg1.AddEntry(h3,'h3')
leg1.AddEntry(nh3,'nh3')

leg2 = ROOT.TLegend(0.6,0.2,0.9,0.6)
leg2.AddEntry(cdf1,'cdf1')
leg2.AddEntry(cdf2,'cdf2')
leg2.AddEntry(cdf3,'cdf3')
leg2.AddEntry(ncdf3,'ncdf3')

C1 = ROOT.TCanvas('c1','c1',800,600)
C1.cd()

h1.Draw("hist")
h2.Draw("hist same")
h3.Draw("hist same")
nh3.Draw("hist same")
leg1.Draw()

C2 = ROOT.TCanvas('c2','c2',800,600)
C2.cd()

cdf1.Draw("hist")
cdf2.Draw("hist same")
cdf3.Draw("hist same")
ncdf3.Draw("hist same")
leg2.Draw()

