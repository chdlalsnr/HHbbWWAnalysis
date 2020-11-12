import os
import copy
import ROOT
import yaml
from array import array

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(False)

era = 2016

nonstitched_dir = f'/home/users/f/b/fbury/bamboodev/HHbbWWAnalysis/BambooOutputHHtobbWW/full{era}NanoV6_WithoutWJetsStitching/results'
stitched_dir = f'/home/users/f/b/fbury/bamboodev/HHbbWWAnalysis/BambooOutputHHtobbWW/full{era}NanoV6_WithWJetsStitching/results'

#var = 'LHE_HT_finer'
#label = 'LHE HT [GeV]'
var = 'LHE_Njets'
label = 'LHE N(jets)'

jet_samples = ['W1JetsToLNu.root',
               'W2JetsToLNu.root',
               'W3JetsToLNu.root',
               'W4JetsToLNu.root']
HT_samples = ['WJetsToLNu_HT-100To200.root',
              'WJetsToLNu_HT-1200To2500.root',
              'WJetsToLNu_HT-200To400.root',
              'WJetsToLNu_HT-2500ToInf.root',
              'WJetsToLNu_HT-400To600.root',
              'WJetsToLNu_HT-600To800.root',
              'WJetsToLNu_HT-70To100.root',
              'WJetsToLNu_HT-800To1200.root']
inc_samples = ['WJetsToLNu.root']

def returnHist(list_samples):
    base_path = os.path.dirname(os.path.dirname(list_samples[0]))
    hist = None
    for rootfile in list_samples:
        sample = os.path.basename(rootfile)
        f = ROOT.TFile(rootfile)
        h = copy.deepcopy(f.Get(var))
        if hist is None:
            hist = h
        else:
            hist.Add(h)
    f.Close()
    return hist

h_HT  = returnHist([os.path.join(nonstitched_dir,sample) for sample in HT_samples])
h_jet = returnHist([os.path.join(nonstitched_dir,sample) for sample in jet_samples])
h_inc = returnHist([os.path.join(nonstitched_dir,sample) for sample in inc_samples])
h_excl_stitch = returnHist([os.path.join(stitched_dir,sample) for sample in jet_samples+HT_samples])
h_excl_all = returnHist([os.path.join(stitched_dir,sample) for sample in jet_samples+HT_samples+inc_samples])

h_HT.SetLineColor(ROOT.kBlue)
h_jet.SetLineColor(ROOT.kOrange)
h_inc.SetLineColor(ROOT.kGreen)
h_excl_stitch.SetLineColor(ROOT.kRed)
h_excl_stitch.SetLineStyle(2)
h_excl_all.SetLineColor(ROOT.kMagenta)
h_excl_all.SetLineStyle(2)

leg = ROOT.TLegend(0.7,0.7,0.9,0.9)
leg.AddEntry(h_HT,'LO W+jets (HT-binned)')
leg.AddEntry(h_jet,'LO W+jets (Njet-binned)')
leg.AddEntry(h_inc,'LO W+jets (inclusive)')
leg.AddEntry(h_excl_stitch,'LO W+jets (exclusive stitched)')
leg.AddEntry(h_excl_all,'LO W+jets (all stitched)')

C = ROOT.TCanvas("C","C",800,600)
C.SetLogy()
h_HT.SetMaximum(max([h.GetMaximum() for h in [h_HT,h_jet,h_inc,h_excl_stitch,h_excl_all]])*3)
h_HT.GetXaxis().SetTitle(label)
h_HT.GetYaxis().SetTitle("# events (weighted)")
h_HT.Draw("hist")
h_jet.Draw("hist same")
h_inc.Draw("hist same")
h_excl_stitch.Draw("hist same")
h_excl_all.Draw("hist same")
leg.Draw()

C.Print(f'plot_Wjets_stitching_{var}_{era}.pdf')

C.Clear()
name = f"WJets_{var}_per_sample_{era}.pdf"
C.Print(name+'[')

for sample in jet_samples+HT_samples+inc_samples:
    for dname,d in zip(['stitched','non stitched'],[stitched_dir,nonstitched_dir]):
        list_samp = [os.path.join(d,sample)]
        h = returnHist(list_samp)
        h.SetTitle('Sample %s [%s]'%(sample.replace('.root',''),dname)+';'+label)
        h.SetMaximum()
        h.Draw("hist")
        C.Print(name)

C.Print(name+']')

