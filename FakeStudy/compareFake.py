import sys
import os
import yaml
import argparse
from pprint import pprint

class CompareFake:
    def __init__(self,path,yamlName,era):
        config = self.extractYAML(os.path.join(path,yamlName))

        config_fake = self.produceFakeYAML(config)

        self.saveYAML(path,yamlName,config_fake,era,"contribution")
        self.saveYAML(path,yamlName,config_fake,era,"comparison")

    @staticmethod
    def extractYAML(path_yaml):
        with open(path_yaml,'r') as handle:
            config = yaml.load(handle,Loader=yaml.FullLoader)
        return config

    @staticmethod
    def produceFakeYAML(config):
        new_config = {}

        # Get files with fake contribution #
        new_config['files'] = {smp:cmpCfg for smp,cmpCfg in config['files'].items() if 'group' in cmpCfg.keys() and cmpCfg['group']=='Fake'}
            
        # Copy other elements #
        new_config['configuration'] = config['configuration']
        new_config['groups'] = {name:config['groups'][name] for name in config['groups'].keys() if name == "Fake"}
        new_config['legend'] = config['legend']
        new_config['plots'] = config['plots']
        new_config['systematics'] = config['systematics']

        return new_config

    @staticmethod
    def saveYAML(path,yamlName,config,era,mode):
        assert mode == "comparison" or mode == "contribution"

        print (path,yamlName)
        if mode == 'contribution':
            out_path = os.path.join(path,yamlName.replace('.yml','')+'Contribution_'+era)
            path_yaml = os.path.join(path,yamlName.replace('.yml','Contribution.yml'))
        if mode == 'comparison':
            out_path = os.path.join(path,yamlName.replace('.yml','')+'Comparison_'+era)
            path_yaml = os.path.join(path,yamlName.replace('.yml','Comparison.yml'))
            # Change BR for MC #
            for smp,smpCfg in config['files'].items():
                if 'branching-ratio' in smpCfg.keys():
                    del config['files'][smp]['branching-ratio']
                else:
                    config['files'][smp] = {'type':'data','group':'data','era':era}
            config['groups']['data'] = {'legend':'Data Fake CR'}
            config['groups']['Fake'].update({'legend':'MC fake CR'})
                    
            
        # Save yaml #
        with open(path_yaml,'w') as handle:
            yaml.dump(config,handle)
        print ("Saved new YAML in %s"%(path_yaml))

        # Print plotIt command #
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        cmd = "plotIt -i {input} -o {output} -y -e {era} {yaml}".format(**{'input': path,
                                                                           'output': out_path,
                                                                           'era': era,
                                                                           'yaml': path_yaml})
        print ("PlotIt command (in bamboo env) : ")
        print (cmd)





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Produce plotIt yaml for Fake comparison')
    parser.add_argument('--path', action='store', required=True, type=str,
                        help='Bamboo output path')
    parser.add_argument('--yaml', action='store', required=True, type=str,
                        help='Name of the yaml')
    parser.add_argument('--era', action='store', required=True, type=str,
                        help='Era')

    args = parser.parse_args()

    instance = CompareFake(args.path,args.yaml,args.era)
