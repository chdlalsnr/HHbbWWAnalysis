import sys
import ROOT

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(False)

f = ROOT.TFile(sys.argv[1])

h1 = f.Get('h1')
h2 = f.Get('h2')
h3 = f.Get('h3')
nh3 = f.Get('nh3')
ZVeto_2b = f.Get('ZVeto_2b')

leg1 = ROOT.TLegend(0.6,0.6,0.85,0.85)
leg1.AddEntry(h1,'Z peak 0b')
leg1.AddEntry(h2,'Z peak 2b')
leg1.AddEntry(h3,'Z veto 0b')
leg1.AddEntry(nh3,'Z veto 2b [extrapolated]')
leg1.AddEntry(ZVeto_2b,'Z veto 2b [MC]')

h1.SetLineColor(ROOT.kRed+1)
h2.SetLineColor(ROOT.kBlue+1)
h3.SetLineColor(ROOT.kGreen+1)
nh3.SetLineColor(ROOT.kMagenta+1)
ZVeto_2b.SetLineColor(ROOT.kOrange+2)

cdf1 = f.Get('cdf1')
cdf2 = f.Get('cdf2')
cdf3 = f.Get('cdf3')
ncdf3 = f.Get('ncdf3')
cdf_ZVeto_2b = f.Get('cdf_ZVeto_2b')

leg2 = ROOT.TLegend(0.6,0.6,0.85,0.85)
leg2.AddEntry(cdf1,'Z peak 0b')
leg2.AddEntry(cdf2,'Z peak 2b')
leg2.AddEntry(cdf3,'Z veto 0b')
leg2.AddEntry(ncdf3,'Z veto 2b [extrapolated]')
leg2.AddEntry(cdf_ZVeto_2b,'Z veto 2b [MC]')

cdf1.SetLineColor(ROOT.kRed+1)
cdf2.SetLineColor(ROOT.kBlue+1)
cdf3.SetLineColor(ROOT.kGreen+1)
ncdf3.SetLineColor(ROOT.kMagenta+1)
cdf_ZVeto_2b.SetLineColor(ROOT.kOrange+2)

c1 = ROOT.TCanvas('c1','c1',800,600)

h1.GetYaxis().SetRangeUser(0.,0.5)
h1.SetTitle('Histograms')
h1.Draw("hist")
h2.Draw("hist same")
h3.Draw("hist same")
nh3.Draw("hist same")
ZVeto_2b.Draw("hist same")
leg1.Draw()

c1.Print(sys.argv[1].replace('.root','_hist.pdf'))

c2 = ROOT.TCanvas('c2','c2',800,600)

cdf1.SetTitle('CDF')
cdf1.GetYaxis().SetRangeUser(0.,1.)
cdf1.Draw("hist")
cdf2.Draw("hist same")
cdf3.Draw("hist same")
ncdf3.Draw("hist same")
cdf_ZVeto_2b.Draw("hist same")
leg2.Draw()

c2.Print(sys.argv[1].replace('.root','_cdf.pdf'))
