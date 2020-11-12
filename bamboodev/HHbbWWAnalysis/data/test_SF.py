import sys
import os
from cppyy import gbl
import json
from pprint import pprint
import itertools

gbl.gSystem.Load(os.path.join(os.environ["VIRTUAL_ENV"], "lib/python3.7/site-packages/libBinnedValues.so"))
gbl.gInterpreter.AddIncludePath(os.path.join(os.environ["VIRTUAL_ENV"], "lib/python3.7/site-packages/bamboo/include"))
gbl.gROOT.ProcessLine('#include "BinnedValues.h"')
gbl.gROOT.ProcessLine('#include "BinnedValuesJSONParser.h"')

json_file = sys.argv[1]
sf = gbl.BinnedValuesJSONParser.parse_file(json_file)

with open(json_file,'r') as handle:
    d = json.load(handle)

xvals = [(d['binning']['x'][i+1]+d['binning']['x'][i])/2 for i in range(0,len(d['binning']['x'])-1)]
yvals = [(d['binning']['y'][i+1]+d['binning']['y'][i])/2 for i in range(0,len(d['binning']['y'])-1)]
data = d['data']
var = d['variables']

def findBin(x,y):
    for d in data:
        if x >= d['bin'][0] and x <= d['bin'][1]:
            for val in d['values']:
                if y >= val['bin'][0] and y <= val['bin'][1]:
                    return [val['value'],val['error_low'],val['error_high']]

params = gbl.Parameters()
for x,y in itertools.product(xvals,yvals):
    params.setEta(x)
    params.setPt(y)
    cont = findBin(x,y)
    res = [r for r in sf.get(params)]
    s = "{}: {:6.2f}, {} : {:6.2f}".format(var[0],x,var[1],y)
    if abs(cont[0]-res[0])/max(1e-6,cont[0]) > 1e-7:
        print ('Wrong value')
        print (s,'-> Json content',cont)
        print (' '*len(s),'-> Tool content',res)
