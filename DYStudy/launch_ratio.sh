#!/bin/bash

python weightDY.py leadjetPt_2016.yml &> /dev/null &
python weightDY.py leadjetPt_2017.yml &> /dev/null &
python weightDY.py leadjetPt_2018.yml &> /dev/null &

python weightDY.py fatjetPt_2016.yml &> /dev/null &
python weightDY.py fatjetPt_2017.yml &> /dev/null &
python weightDY.py fatjetPt_2018.yml &> /dev/null &

python weightDY.py fatjetSoftDropMass_2016.yml &> /dev/null &
python weightDY.py fatjetSoftDropMass_2017.yml &> /dev/null &
python weightDY.py fatjetSoftDropMass_2018.yml &> /dev/null &
