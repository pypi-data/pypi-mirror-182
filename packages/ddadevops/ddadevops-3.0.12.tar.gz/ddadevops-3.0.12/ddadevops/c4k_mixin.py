from os import chmod
from string import Template
from subprocess import run
from .python_util import *
from .devops_build import DevopsBuild

def add_c4k_mixin_config(config,
                         c4k_module_name=None,
                         c4k_config_dict=None,
                         c4k_auth_dict=None):
    if c4k_module_name == None:
        c4k_module_name = 'NO_MODULE'
    if c4k_config_dict == None:                         
        c4k_config_dict = {}
    if c4k_auth_dict == None:                         
        c4k_auth_dict = {}
    
    config.update({'C4kMixin': {'Config': c4k_config_dict,
                                'Auth': c4k_auth_dict,
                                'Name': c4k_module_name}})
    return config


def generate_clojure_map(template_dict):
    clojure_map_str = '{'
    for key, value in template_dict.items():
        clojure_map_str += f':{key} "{value}"\n'
    clojure_map_str += '}'
    return clojure_map_str


class C4kMixin(DevopsBuild):

    def __init__(self, project, config):
        super().__init__(project, config)
        self.c4k_mixin_config = config['C4kMixin']['Config']
        self.c4k_mixin_auth = config['C4kMixin']['Auth']
        self.c4k_module_name = config['C4kMixin']['Name']

    def write_c4k_config(self):
        fqdn = self.get('fqdn')
        self.c4k_mixin_config.update({'fqdn':fqdn})
        with open(self.build_path() + '/out_config.edn', 'w') as output_file:
            output_file.write(generate_clojure_map(self.c4k_mixin_config))
    
    def write_c4k_auth(self):
        with open(self.build_path() + '/out_auth.edn', 'w') as output_file:
            output_file.write(generate_clojure_map(self.c4k_mixin_auth))
        chmod(self.build_path() + '/out_auth.edn', 0o600)

    def c4k_apply(self):
        cmd = [f'c4k-{self.c4k_module_name}-standalone.jar',
               self.build_path() + '/out_config.edn',
               self.build_path() + '/out_auth.edn', 
               '> ' + self.build_path() + '/out_jitsi.yaml']
        output = execute(cmd, True)
        print(output)
        return output
