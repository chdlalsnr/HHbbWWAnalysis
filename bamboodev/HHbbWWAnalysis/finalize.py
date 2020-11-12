import os
import sys
import subprocess


def finalize(path,verbose=False):
    path = os.path.abspath(path)

    with open(os.path.join(path,'batch','input','cluster_id'),'r') as f:
        cluster_id = f.readline()

    p = subprocess.Popen(['sacct', '-j', cluster_id, '--format=jobid%15,State', '-X', '--noheader'], stdout=subprocess.PIPE)
    out, _ = p.communicate()
    status = {}
    for line in out.decode("utf-8").splitlines():
        n, s = line.split()
        n = n.replace(cluster_id+"_","")
        status[n] = s

    state = ["COMPLETED","FAILED","TIMEOUT","OUT_OF_MEMORY","CANCELLED"]
    for s in state:
        print (("   Status %s"%s).ljust(30,' ')+"%4d jobs / %d"%(sum(v==s for v in status.values()),len(status.keys())))

    content = {}
    for num in status.keys():
        p = os.path.join(path,'batch','output',num)
        if not os.path.exists(p):
            content[p] = None
        else:
            content[p] = os.listdir(p)[0] if len(os.listdir(p))!=0 else ''

    if None in content.values():
        print ("Some outputs are missing")
        sbatch_cmd = "sbatch --array="
        list_num = [os.path.basename(k) for k,v in content.items() if v is None]
        sbatch_cmd += ','.join(list_num)+" "

        with open(os.path.expanduser("~/.config/bamboorc"),'r') as f:
            for line in f:
                if line.startswith('sbatch_partition'):
                    sbatch_cmd += "--partition=%s "%line.split()[-1]
                if line.startswith('sbatch_qos'):
                    sbatch_cmd += "--qos=%s "%line.split()[-1]
                if line.startswith('sbatch_time'):
                    sbatch_cmd += "--time=%s "%line.split()[-1]
                if line.startswith('sbatch_mem'):
                    sbatch_cmd += "--mem-per-cpu=%s "%line.split()[-1]
                if line.startswith('sbatch_additionalOptions'):
                    sbatch_cmd += ' '.join(line.split()[2:]).replace(',','')+" "
        sbatch_cmd += " "+os.path.join(path,'batch','slurmSubmission.sh')
        print ("Command to resubmit them is below")
        print (sbatch_cmd)
    else:
        print ("All the outputs are present, will hadd them now") 
        samples = sorted(list(set(content.values())))
        for sample in samples:
            if sample is '':
                continue
            list_sample = [os.path.join(k,v) for k,v in content.items() if v==sample]
            cmd = ['hadd','-f',os.path.join(path,'results',sample)]+list_sample
            if verbose:
                print ("Command : ",' '.join(cmd))
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            out, _ = p.communicate()
            print ("   Produced file %s"%os.path.join(path,'results',sample))


finalize(sys.argv[1],False)
