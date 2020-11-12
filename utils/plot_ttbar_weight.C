
void plot_ttbar_weight(std::string path){
    gStyle->SetOptStat(0);
    TFile* f = new TFile(path.c_str());
    TH3F* h = (TH3F*)f->Get("ttbar_weight_vs_pt");

    h->SetTitle("t#bar{t} weights as function of t and #bar{t} P_{T};P_{T}(t);P_{T}(#bar{t});t#bar{t} weight");
    h->GetXaxis()->SetTitleOffset(1.5);
    h->GetYaxis()->SetTitleOffset(1.5);
    h->GetZaxis()->SetTitleOffset(1.5);

    TCanvas *c = new TCanvas("c","c",800,600);
    c->SetRightMargin(2.1);
    c->SetLeftMargin(1.5);
    c->SetBottomMargin(1.5);
    c->Update();

    c->cd();
    h->Draw("BOX2Z");
    

    TH2F *hProjTopPt = (TH2F*)h->Project3D("zx");
    hProjTopPt->SetTitle("t#bar{t} weights as function of top P_{T};P_{T}(t);t#bar{t} weight");
    TH2F *hProjAntitopPt = (TH2F*)h->Project3D("zy");
    hProjAntitopPt->SetTitle("t#bar{t} weights as function of antitop P_{T};P_{T}(#bar{t});t#bar{t} weight");

    TCanvas *cx = new TCanvas("cx","cx",800,600);
    cx->cd();
    hProjTopPt->Draw("colz");

    TCanvas *cy = new TCanvas("cy","cy",800,600);
    cy->cd();
    hProjAntitopPt->Draw("colz");
}

