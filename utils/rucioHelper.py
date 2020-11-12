import os
import sys
import subprocess

def readTextFile(path):
    with open(path, "r") as f:
        alist = [line.strip() for line in f if len(line)!=0]
    alist = [l for l in alist if len(l)!=0]
    return alist

def getRucioList(user):
    cmd = ['rucio','list-rules','--account=fbury']
    lines = subprocess.check_output(cmd).decode().split('\n')
    datasets = []
    for i in range(2,len(lines)): # two first lines are header
        line = lines[i].split()
        if len (line) == 0:
            continue
        # order : 0 -> tag
        #         1 -> user
        #         2 -> cms:datatet
        #         3 -> state
        #         4 -> site
        #         5 -> # copies
        #         6 -> date
        #         7 -> time
        dataset = line[2].replace('cms:','')
        if line[3].startswith('OK'):
            state = 'OK'
        elif line[3].startswith('REPL'):
            state = "REPLICATING"
        elif line[3].startswith('STUC'):
            state = "STUCK"
        else:
            raise ValueError("Unknown state %s"%line[3])
        datasets.append({'dataset':dataset,'state':state})

    datasets_ok    = [d['dataset'] for d in datasets if d['state']=='OK']
    datasets_repl  = [d['dataset'] for d in datasets if d['state']=='REPLICATING']
    datasets_stuck = [d['dataset'] for d in datasets if d['state']=='STUCK']
    print ("Status :")
    print ("... OK          : %4d / %4d [%3.2f%%]"%(len(datasets_ok),len(datasets),len(datasets_ok)*100/len(datasets)))
    print ("... REPLICATING : %4d / %4d [%3.2f%%]"%(len(datasets_repl),len(datasets),len(datasets_repl)*100/len(datasets)))
    print ("... STUCK       : %4d / %4d [%3.2f%%]"%(len(datasets_stuck),len(datasets),len(datasets_stuck)*100/len(datasets)))
    return [d['dataset'] for d in datasets]

def requestDatasets(txtfile,user):
    rucio_datasets = getRucioList(user)
    list_datasets = readTextFile(txtfile)
    missing_datasets = [d for d in list_datasets if d not in rucio_datasets]
    print ('Importing from text file %s'%txtfile)
    print ("Datasets in Rucio     : %5d"%len(rucio_datasets))
    print ("Datasets in text file : %5d"%len(list_datasets))
    print ("Missing datasets      : %5d"%len(missing_datasets))
    print ('Will request the datasets on Rucio')
    for dataset in missing_datasets:
        cmd = ['rucio','add-rule','cms:'+dataset,'1','T2_BE_UCL']
        try:
            tag = subprocess.check_output(cmd).decode()
            print ('... Requested dataset %s -> tag : %s'%(dataset,tag))
        except subprocess.CalledProcessError:
            print ("... Data identifier cms:%s not found"%dataset)

    

#list_nano = requestDatasets('signal_nanoaod_samples_2016_v6.txt','fbury')
#list_nano = requestDatasets('signal_nanoaod_samples_2017_v6.txt','fbury')
#list_nano = requestDatasets('signal_nanoaod_samples_2018_v6.txt','fbury')
#list_nano = requestDatasets('background_nanoaod_samples_2016_v6.txt','fbury')
#list_nano = requestDatasets('background_nanoaod_samples_2017_v6.txt','fbury')
#list_nano = requestDatasets('background_nanoaod_samples_2018_v6.txt','fbury')
#list_nano = requestDatasets('data_nanoaod_samples_2016_Nano25Oct2019.txt','fbury')
#list_nano = requestDatasets('data_nanoaod_samples_2017_Nano25Oct2019.txt','fbury')
#list_nano = requestDatasets('data_nanoaod_samples_2018_Nano25Oct2019.txt','fbury')
#list_nano = requestDatasets('signal_nanoaod_samples_2016_v7.txt','fbury')
#list_nano = requestDatasets('signal_nanoaod_samples_2017_v7.txt','fbury')
#list_nano = requestDatasets('signal_nanoaod_samples_2018_v7.txt','fbury')
#list_nano = requestDatasets('background_nanoaod_samples_2016_v7.txt','fbury')
#list_nano = requestDatasets('background_nanoaod_samples_2017_v7.txt','fbury')
#list_nano = requestDatasets('background_nanoaod_samples_2018_v7.txt','fbury')
#list_nano = requestDatasets('data_nanoaod_samples_02Apr2020.txt','fbury')
list_nano = requestDatasets('all_nanoaod_mc.txt','fbury')
#list_nano = requestDatasets('all_nanoaod_data.txt','fbury')
