#!/bin/bash

#bambooRun -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2016_v7_MC.yml -o BtagReweightingOn --BtagReweightingOn --NoSystematics --distributed=driver
#bambooRun -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2016_v7_MC.yml -o BtagReweightingOff --BtagReweightingOff --NoSystematics --distributed=driver
#bambooRun -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2016_v7_signal.yml -o BtagReweightingOn_signal --BtagReweightingOn --NoSystematics --distributed=driver
#bambooRun -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2016_v7_signal.yml -o BtagReweightingOff_signal --BtagReweightingOff --NoSystematics --distributed=driver

#bambooRun -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2016_v6_MC.yml -o BtagReweightingOn --BtagReweightingOn --NoSystematics --distributed=driver
#bambooRun -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2016_v6_MC.yml -o BtagReweightingOff --BtagReweightingOff --NoSystematics --distributed=driver
#bambooRun -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2016_v6_signal.yml -o BtagReweightingOn_signal --BtagReweightingOn --NoSystematics --distributed=driver
#bambooRun -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2016_v6_signal.yml -o BtagReweightingOff_signal --BtagReweightingOff --NoSystematics --distributed=driver

bambooRun -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2016_v7.yml -o bbww_2016v7_boosted_woak8btag --NoSystematics --Tight --Boosted1Btag --distributed=finalize
#bambooRun -m BtagEffAndMistag.py:BtagEffAndMistagNano analysis2016_v7.yml -o bbww_2016v7_effwoak8 --NoSystematics --Tight --Boosted --distributed=driver
#bambooRun -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2016_v7_MC.yml -o dummy --NoSystematics --Tight --Boosted --maxFiles=1
#bambooRun -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2016_v7_signal.yml -o bbww_2016v7_boosted_signal --NoSystematics --Tight --Boosted --distributed=driver

#bambooRun -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2016_v6.yml -o bbww_2016v6_boosted --NoSystematics --Tight --Boosted --distributed=driver #--onlypost #--distributed=finalize
#bambooRun -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2017_v6.yml -o bbww_2017 --Tight --NoSystematics --Resolved2Btag --distributed=driver #--onlypost #--distributed=finalize
#bambooRun -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2018_v6.yml -o bbww_2018 --Tight --NoSystematics --Resolved2Btag --onlypost #--distributed=finalize

#bambooRun -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL test.yml -o test --NoSystematics --Preselected --Resolved2Btag
