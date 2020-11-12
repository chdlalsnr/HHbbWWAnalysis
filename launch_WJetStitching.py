#!/bin/bash

bambooRun --distributed=driver -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2016_v6_WJets.yml -o BambooOutputHHtobbWW/full2016NanoV6_WithWJetsStitching_v3  --WJetsStitchingPlots &
bambooRun --distributed=driver -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2017_v6_WJets.yml -o BambooOutputHHtobbWW/full2017NanoV6_WithWJetsStitching_v3  --WJetsStitchingPlots & 
bambooRun --distributed=driver -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2018_v6_WJets.yml -o BambooOutputHHtobbWW/full2018NanoV6_WithWJetsStitching_v3  --WJetsStitchingPlots &
bambooRun --distributed=driver -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2016_v6_WJets.yml -o BambooOutputHHtobbWW/full2016NanoV6_WithoutWJetsStitching_v3  --WJetsStitchingPlots --NoStitching &
bambooRun --distributed=driver -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2017_v6_WJets.yml -o BambooOutputHHtobbWW/full2017NanoV6_WithoutWJetsStitching_v3  --WJetsStitchingPlots --NoStitching &
bambooRun --distributed=driver -m PlotterHHtobbWWDL.py:PlotterNanoHHtobbWWDL analysis2018_v6_WJets.yml -o BambooOutputHHtobbWW/full2018NanoV6_WithoutWJetsStitching_v3  --WJetsStitchingPlots --NoStitching &
