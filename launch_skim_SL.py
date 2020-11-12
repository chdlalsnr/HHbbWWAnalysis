import os
import sys
import re
import subprocess
import shutil
import argparse
import time
import ROOT
from utils.finalize import finalize

parser = argparse.ArgumentParser(description='Launch Skim production')
parser.add_argument('--remove', action='store_true', required=False, default=False,
                    help='Clears the directories')
parser.add_argument('--send', action='store_true', required=False, default=False,
                    help='Sends the jobs')
parser.add_argument('--resubmit', action='store_true', required=False, default=False,
                    help='Resubmit the jobs')
parser.add_argument('--debug', action='store_true', required=False, default=False,
                    help='Print the resubmit commands without sending them')
parser.add_argument('--id', action='store_true', required=False, default=False,
                    help='Return ID of the sent jobs')
parser.add_argument('--era', action='store', required=True, type=str,
                    help='Era')
args = parser.parse_args()

era = args.era

cmd = [['bambooRun','--distributed=driver','-m','SkimmerHHtobbWWSL.py:SkimmerNanoHHtobbWWSL',f'analysis{era}_v6_MC.yml','--Tight','--LooseResolved0b3j','--Channel','El','-o',f'/nfs/scratch/fynu/gsaha/BambooOutputHHtobbWW/SkimSL{era}_Background_LooseResolved0b3j_El'],
      ['bambooRun','--distributed=driver','-m','SkimmerHHtobbWWSL.py:SkimmerNanoHHtobbWWSL',f'analysis{era}_v6_MC.yml','--Tight','--LooseResolved0b3j','--Channel','Mu','-o',f'/nfs/scratch/fynu/gsaha/BambooOutputHHtobbWW/SkimSL{era}_Background_LooseResolved0b3j_Mu'],
      ['bambooRun','--distributed=driver','-m','SkimmerHHtobbWWSL.py:SkimmerNanoHHtobbWWSL',f'analysis{era}_v6_MC.yml','--Tight','--LooseResolved1b2j','--Channel','El','-o',f'/nfs/scratch/fynu/gsaha/BambooOutputHHtobbWW/SkimSL{era}_Background_LooseResolved1b2j_El'],
      ['bambooRun','--distributed=driver','-m','SkimmerHHtobbWWSL.py:SkimmerNanoHHtobbWWSL',f'analysis{era}_v6_MC.yml','--Tight','--LooseResolved1b2j','--Channel','Mu','-o',f'/nfs/scratch/fynu/gsaha/BambooOutputHHtobbWW/SkimSL{era}_Background_LooseResolved1b2j_Mu'],
      ['bambooRun','--distributed=driver','-m','SkimmerHHtobbWWSL.py:SkimmerNanoHHtobbWWSL',f'analysis{era}_v6_MC.yml','--Tight','--LooseResolved2b1j','--Channel','El','-o',f'/nfs/scratch/fynu/gsaha/BambooOutputHHtobbWW/SkimSL{era}_Background_LooseResolved2b1j_El'],
      ['bambooRun','--distributed=driver','-m','SkimmerHHtobbWWSL.py:SkimmerNanoHHtobbWWSL',f'analysis{era}_v6_MC.yml','--Tight','--LooseResolved2b1j','--Channel','Mu','-o',f'/nfs/scratch/fynu/gsaha/BambooOutputHHtobbWW/SkimSL{era}_Background_LooseResolved2b1j_Mu'],
      ['bambooRun','--distributed=driver','-m','SkimmerHHtobbWWSL.py:SkimmerNanoHHtobbWWSL',f'analysis{era}_v6_MC.yml','--Tight','--TightResolved0b4j','--Channel','El','-o',f'/nfs/scratch/fynu/gsaha/BambooOutputHHtobbWW/SkimSL{era}_Background_TightResolved0b4j_El'],
      ['bambooRun','--distributed=driver','-m','SkimmerHHtobbWWSL.py:SkimmerNanoHHtobbWWSL',f'analysis{era}_v6_MC.yml','--Tight','--TightResolved0b4j','--Channel','Mu','-o',f'/nfs/scratch/fynu/gsaha/BambooOutputHHtobbWW/SkimSL{era}_Background_TightResolved0b4j_Mu'],
      ['bambooRun','--distributed=driver','-m','SkimmerHHtobbWWSL.py:SkimmerNanoHHtobbWWSL',f'analysis{era}_v6_MC.yml','--Tight','--TightResolved1b3j','--Channel','El','-o',f'/nfs/scratch/fynu/gsaha/BambooOutputHHtobbWW/SkimSL{era}_Background_TightResolved1b3j_El'],
      ['bambooRun','--distributed=driver','-m','SkimmerHHtobbWWSL.py:SkimmerNanoHHtobbWWSL',f'analysis{era}_v6_MC.yml','--Tight','--TightResolved1b3j','--Channel','Mu','-o',f'/nfs/scratch/fynu/gsaha/BambooOutputHHtobbWW/SkimSL{era}_Background_TightResolved1b3j_Mu'],
      ['bambooRun','--distributed=driver','-m','SkimmerHHtobbWWSL.py:SkimmerNanoHHtobbWWSL',f'analysis{era}_v6_MC.yml','--Tight','--TightResolved2b2j','--Channel','El','-o',f'/nfs/scratch/fynu/gsaha/BambooOutputHHtobbWW/SkimSL{era}_Background_TightResolved2b2j_El'],
      ['bambooRun','--distributed=driver','-m','SkimmerHHtobbWWSL.py:SkimmerNanoHHtobbWWSL',f'analysis{era}_v6_MC.yml','--Tight','--TightResolved2b2j','--Channel','Mu','-o',f'/nfs/scratch/fynu/gsaha/BambooOutputHHtobbWW/SkimSL{era}_Background_TightResolved2b2j_Mu'],
      ['bambooRun','--distributed=driver','-m','SkimmerHHtobbWWSL.py:SkimmerNanoHHtobbWWSL',f'analysis{era}_v6_MC.yml','--Tight','--SemiBoostedHbbWtoJ','--Channel','El','-o',f'/nfs/scratch/fynu/gsaha/BambooOutputHHtobbWW/SkimSL{era}_Background_SemiBoostedHbbWtoJ_El'],
      ['bambooRun','--distributed=driver','-m','SkimmerHHtobbWWSL.py:SkimmerNanoHHtobbWWSL',f'analysis{era}_v6_MC.yml','--Tight','--SemiBoostedHbbWtoJ','--Channel','Mu','-o',f'/nfs/scratch/fynu/gsaha/BambooOutputHHtobbWW/SkimSL{era}_Background_SemiBoostedHbbWtoJ_Mu'],
      ['bambooRun','--distributed=driver','-m','SkimmerHHtobbWWSL.py:SkimmerNanoHHtobbWWSL',f'analysis{era}_v6_MC.yml','--Tight','--SemiBoostedHbbWtoJJ','--Channel','El','-o',f'/nfs/scratch/fynu/gsaha/BambooOutputHHtobbWW/SkimSL{era}_Background_SemiBoostedHbbWtoJJ_El'],
      ['bambooRun','--distributed=driver','-m','SkimmerHHtobbWWSL.py:SkimmerNanoHHtobbWWSL',f'analysis{era}_v6_MC.yml','--Tight','--SemiBoostedHbbWtoJJ','--Channel','Mu','-o',f'/nfs/scratch/fynu/gsaha/BambooOutputHHtobbWW/SkimSL{era}_Background_SemiBoostedHbbWtoJJ_Mu'],
      ['bambooRun','--distributed=driver','-m','SkimmerHHtobbWWSL.py:SkimmerNanoHHtobbWWSL',f'analysis{era}_v6_MC.yml','--Tight','--SemiBoostedWjj','--Channel','El','-o',f'/nfs/scratch/fynu/gsaha/BambooOutputHHtobbWW/SkimSL{era}_Background_SemiBoostedWjj_El'],
      ['bambooRun','--distributed=driver','-m','SkimmerHHtobbWWSL.py:SkimmerNanoHHtobbWWSL',f'analysis{era}_v6_MC.yml','--Tight','--SemiBoostedWjj','--Channel','Mu','-o',f'/nfs/scratch/fynu/gsaha/BambooOutputHHtobbWW/SkimSL{era}_Background_SemiBoostedWjj_Mu'],
      ['bambooRun','--distributed=driver','-m','SkimmerHHtobbWWSL.py:SkimmerNanoHHtobbWWSL',f'analysis{era}_v6_MC.yml','--Tight','--Boosted','--Channel','El','-o',f'/nfs/scratch/fynu/gsaha/BambooOutputHHtobbWW/SkimSL{era}_Background_Boosted_El'],
      ['bambooRun','--distributed=driver','-m','SkimmerHHtobbWWSL.py:SkimmerNanoHHtobbWWSL',f'analysis{era}_v6_MC.yml','--Tight','--Boosted','--Channel','Mu','-o',f'/nfs/scratch/fynu/gsaha/BambooOutputHHtobbWW/SkimSL{era}_Background_Boosted_Mu']]


def remove():
    for c in cmd:
        path = c[-1]
        if os.path.exists(path):
            shutil.rmtree(path)
            print ("Removed %s"%path)

def send():
    for c in cmd:
        path = c[-1]
        if os.path.exists(path):
            print ('Path exists, will not launch jobs : %s'%path)
        else:
            subprocess.Popen(c)
        #print (' '.join(c))

def getSlurmID():
    cid = []
    for c in cmd:
        path = c[-1]
        c_id_path = os.path.join(path,'batch','input','cluster_id') 
        with open(c_id_path,'r') as f:
            cid.append(f.readline())
    print ('ID of jobs')
    print (' '.join(cid))

def resubmit(debug):
    res_cmd = []
    for c in cmd:
        path = c[-1]
        res = finalize(path,False,False,False)
        if res == 0:
            print ('Path %s : complete'%path)
        else:
            res_cmd.append(res)
    print ('='*80)
    print ('Commands to resubmit')
    cid = []
    for c in res_cmd:
        if debug:
            print (c)
        else:
            p = subprocess.Popen([a for a in c.split(' ') if len(a)!=0],stdout=subprocess.PIPE)
            out, err = p.communicate()
            cid.append(int(re.findall(r'\d+',str(out))[0]))
    if debug:
        with open('skim_resubmit.txt','w') as f:
            f.write('\n'.join(res_cmd))
        print ('Commands saved in skim_resubmit.txt')
    else:
        print ('List of resubmit IDs')
        print (' '.join([str(c) for c in cid]))

if args.remove:
    remove()
if args.send:
    send()
if args.id:
    getSlurmID()
if args.resubmit:
    resubmit(args.debug)
