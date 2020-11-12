import yaml
from pprint import pprint

def compareYamlAndTxt(yamlFile, txtFile):
    dasList = []
    with open(yamlFile,"r") as f:
        das = yaml.load(f)['samples']
        for val in das.values():
            if isinstance(val['db'],str):
                dasList.append(val['db'].replace('das:',''))
            elif isinstance(val['db'],list):
                dasList.extend([v.replace('das:','') for v in val['db']]) 
            else:
                raise RuntimeError

    files = []
    with open(txtFile,'r') as f:
        for line in f:
            files.append(line.replace('\n',''))


    missing_das = [f for f in files if f not in dasList]
    missing_txt = [f for f in dasList if f not in files]
    print ('YAML',yamlFile)
    print ('Txt ',txtFile)
    print ('Missing files in yaml')
    pprint (missing_das)
    print ('In yaml but not in txt')
    pprint (missing_txt)

    # Check dascache entries #
    for sample,d in das.items():
        if sample not in d['files']:
            raise RuntimeError('Wrong : %s VS %s'%(sample,d['files']))


compareYamlAndTxt("analysis2016_v6_signal.yml","./utils/signal_nanoaod_samples_2016_v6.txt")
compareYamlAndTxt("analysis2017_v6_signal.yml","./utils/signal_nanoaod_samples_2017_v6.txt")
compareYamlAndTxt("analysis2018_v6_signal.yml","./utils/signal_nanoaod_samples_2018_v6.txt")


