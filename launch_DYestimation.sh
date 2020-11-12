#!/bin/bash

bambooRun --distributed=finalize -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2016_v6.yml -o BambooOutputHHtobbWW/full2016NanoV6_Tight_Fake_DYEstimation_OutputDY_mc --Tight --NoSystematic  --Resolved1Btag --Resolved2Btag --datadriven=all --DYVariable DY  --onlypost &
bambooRun --distributed=finalize -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2016_v6.yml -o BambooOutputHHtobbWW/full2016NanoV6_Tight_Fake_DYEstimation_OutputTT_mc --Tight --NoSystematic  --Resolved1Btag --Resolved2Btag --datadriven=all --DYVariable TT --onlypost  &
bambooRun --distributed=finalize -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2016_v6.yml -o BambooOutputHHtobbWW/full2016NanoV6_Tight_Fake_DYEstimation_OutputST_mc --Tight --NoSystematic  --Resolved1Btag --Resolved2Btag --datadriven=all --DYVariable ST --onlypost  &
bambooRun --distributed=finalize -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2016_v6.yml -o BambooOutputHHtobbWW/full2016NanoV6_Tight_Fake_DYEstimation_OutputH_mc --Tight --NoSystematic  --Resolved1Btag --Resolved2Btag --datadriven=all --DYVariable H --onlypost  &
bambooRun --distributed=finalize -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2016_v6.yml -o BambooOutputHHtobbWW/full2016NanoV6_Tight_Fake_DYEstimation_OutputHH_mc --Tight --NoSystematic  --Resolved1Btag --Resolved2Btag --datadriven=all --DYVariable HH --onlypost  &
bambooRun --distributed=finalize -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2016_v6.yml -o BambooOutputHHtobbWW/full2016NanoV6_Tight_Fake_DYEstimation_OutputTTVX_mc --Tight --NoSystematic  --Resolved1Btag --Resolved2Btag --datadriven=all --DYVariable TTVX --onlypost  &
bambooRun --distributed=finalize -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2016_v6.yml -o BambooOutputHHtobbWW/full2016NanoV6_Tight_Fake_DYEstimation_OutputVVV_mc --Tight --NoSystematic  --Resolved1Btag --Resolved2Btag --datadriven=all --DYVariable VVV --onlypost  &
bambooRun --distributed=finalize -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2016_v6.yml -o BambooOutputHHtobbWW/full2016NanoV6_Tight_Fake_DYEstimation_OutputRare_mc --Tight --NoSystematic  --Resolved1Btag --Resolved2Btag --datadriven=all --DYVariable Rare --onlypost  &

#python utils/finalize.py --path BambooOutputHHtobbWW/full2016NanoV6_Tight_Fake_DYEstimation_OutputDY_mc    &    
#python utils/finalize.py --path BambooOutputHHtobbWW/full2016NanoV6_Tight_Fake_DYEstimation_OutputTT_mc    &
#python utils/finalize.py --path BambooOutputHHtobbWW/full2016NanoV6_Tight_Fake_DYEstimation_OutputST_mc    &
#python utils/finalize.py --path BambooOutputHHtobbWW/full2016NanoV6_Tight_Fake_DYEstimation_OutputH_mc     &
#python utils/finalize.py --path BambooOutputHHtobbWW/full2016NanoV6_Tight_Fake_DYEstimation_OutputHH_mc    &
#python utils/finalize.py --path BambooOutputHHtobbWW/full2016NanoV6_Tight_Fake_DYEstimation_OutputTTVX_mc  &
#python utils/finalize.py --path BambooOutputHHtobbWW/full2016NanoV6_Tight_Fake_DYEstimation_OutputVVV_mc   &
#python utils/finalize.py --path BambooOutputHHtobbWW/full2016NanoV6_Tight_Fake_DYEstimation_OutputRare_mc  &
