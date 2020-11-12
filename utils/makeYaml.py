import yaml
from pprint import pprint
from collections import OrderedDict

daspaths = []
with open("all_nanoaod_mc.txt","r") as f:
    for line in f:
        daspaths.append(line.replace('\n',''))

sig16 = [d for d in daspaths if "HH" in d and "RunIISummer16" in d]
back16 = [d for d in daspaths if "HH" not in d and "RunIISummer16" in d]
sig17 = [d for d in daspaths if "HH" in d and "RunIIFall17" in d]
back17 = [d for d in daspaths if "HH" not in d and "RunIIFall17" in d]
sig18 = [d for d in daspaths if "HH" in d and "RunIIAutumn18" in d]
back18 = [d for d in daspaths if "HH" not in d and "RunIIAutumn18" in d]

with open("../analysis2017_v7_tmp.yml","r") as f:
    d17 = yaml.load(f)

check17 = {}
newd17 = OrderedDict()
newd17['tree'] = d17['tree']
newd17['eras'] = d17['eras']
newd17['samples'] = OrderedDict()
for sample in d17["samples"].keys():
    newd17['samples'][sample] = d17["samples"][sample]
    das_sample = d17["samples"][sample]['db']
    if isinstance(das_sample,list):
        das_sample = das_sample[0]
    name = das_sample.split('/')[1]
    match_daspath = [daspath for daspath in back17 if name in daspath]
    check17[sample] = len(match_daspath) > 0
    if len (match_daspath) == 1:
        newd17["samples"][sample]['db'] = 'das:'+match_daspath[0]
    elif len (match_daspath) > 1:
        match_daspath = ['das:'+m for m in match_daspath]
        newd17["samples"][sample]['db'] = match_daspath

newd17['datadriven'] = d17['datadriven']
newd17['plotIt'] = d17['plotIt']

for k,v in check17.items():
    if not v:
        print("Missing sample %s in yaml"%k)

with open("../analysis2017_v7_test.yml","w") as f:
    yaml.dump(newd17,f)


with open("../analysis2018_v7_tmp.yml","r") as f:
    d18 = yaml.load(f)

check18 = {}
newd18 = OrderedDict()
newd18['tree'] = d18['tree']
newd18['eras'] = d18['eras']
newd18['samples'] = OrderedDict()
for sample in d18["samples"].keys():
    newd18['samples'][sample] = d18["samples"][sample]
    das_sample = d18["samples"][sample]['db']
    if isinstance(das_sample,list):
        das_sample = das_sample[0]
    name = das_sample.split('/')[1]
    match_daspath = [daspath for daspath in back18 if name in daspath]
    check18[sample] = len(match_daspath) > 0
    if len (match_daspath) == 1:
        newd18["samples"][sample]['db'] = 'das:'+match_daspath[0]
    elif len (match_daspath) > 1:
        match_daspath = ['das:'+m for m in match_daspath]
        newd18["samples"][sample]['db'] = match_daspath

newd18['datadriven'] = d18['datadriven']
newd18['plotIt'] = d18['plotIt']

for k,v in check18.items():
    if not v:
        print("Missing sample %s in yaml"%k)

with open("../analysis2018_v7_test.yml","w") as f:
    yaml.dump(newd18,f)

