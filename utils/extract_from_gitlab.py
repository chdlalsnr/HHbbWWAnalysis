import os

samples = []
with open("gitlab_datasets.txt","r") as f:
    for line in f:
        if "MINIAODSIM" in line:
            #lines.append(line)
            sample = [l for l in line.split() if "MINIAODSIM" in l][0]
            sample = sample.replace('<sup>','').replace('</sup>','')
            samples.append(sample)

with open("all_mc_samples.txt","w") as f:
    for sample in samples:
        f.write(sample+'\n')
