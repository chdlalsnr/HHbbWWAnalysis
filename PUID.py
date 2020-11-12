
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/PileupJetID
puIDSFLib = {
        f"{year}_{wp}" : {
            f"{eom}_{mcsf}" :f"PUID_80X_{eom}_{mcsf}_{year}_{wp}.json"           for eom in ("eff", "mistag") for mcsf in ("mc", "sf")
        }
    for year in ("2016", "2017", "2018") for wp in "LMT"
    }
from pprint import pprint
pprint (puIDSFLib)
sys.exit()
import bamboo.scalefactors
def makePUIDSF(jets, year=None, wp=None, wpToCut=None):
    sfwpyr = puIDSFLib[f"{year}_{wp}"]
    sf_eff = bamboo.scalefactors.get_scalefactor("lepton", "eff_sf"   , sfLib=sfwpyr, paramDefs=bamboo.scalefactors.binningVariables_nano)
    sf_mis = bamboo.scalefactors.get_scalefactor("lepton", "mistag_sf", sfLib=sfwpyr, paramDefs=bamboo.scalefactors.binningVariables_nano)
    eff_mc = bamboo.scalefactors.get_scalefactor("lepton", "eff_mc"   , sfLib=sfwpyr, paramDefs=bamboo.scalefactors.binningVariables_nano)
    mis_mc = bamboo.scalefactors.get_scalefactor("lepton", "mistag_mc", sfLib=sfwpyr, paramDefs=bamboo.scalefactors.binningVariables_nano)
    jets_m50 = op.select(jets, lambda j : j.pt < 50.)
    wFail = op.extMethod("scalefactorWeightForFailingObject", returnType="double")
    return op.rng_product(jets_m50, lambda j : op.switch(j.genJet.isValid,
        op.switch(wpToCut[wp](j), sf_eff(j), wFail(sf_eff(j), eff_mc(j))),
        op.switch(wpToCut[wp](j), sf_mis(j), wFail(sf_mis(j), mis_mc(j)))
        ))

