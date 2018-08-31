#!/usr/bin/python3
import os.path as path
import os
import json
import subprocess
import sys

SCRIPTS_DIR = path.join(path.dirname(path.realpath(__file__)), 'scripts')

# print(SCRIPTS_DIR)

def prompt (consts, type_name):
    res = None

    while not res:
        print("Select the %s:" % type_name)

        for index, entry in enumerate(consts):
            print("[%i] %s" % (index + 1, entry))

        try: 
            res = consts[int(input("> ")) - 1]
            print("[I] Selected %s: %s" % (type_name, res))
            print()
        except KeyboardInterrupt:
            sys.exit()
        except: 
            print("[E] Invalid input!")
            print()
        

    return res


def exec_scripts (group, module_path):
    if group["run_common"]:
        subprocess.call([ path.join(module_path, 'common.sh') ])
        print("Running", path.join(module_path, 'common.sh'))


    if not len(group["scripts"]): 
        return
    elif type(group["scripts"]) is str:
        script_path = path.join(module_path, group["scripts"])
        subprocess.call([ script_path ])
        print("Running", script_path)
    else:
        for script in group["scripts"]:
            script_path = path.join(module_path, script)
            subprocess.call([ script ])
            print("Running", script_path)


PLATFORMS = [
    'physical',
    'virtualbox',
    'arm'
]

OS = [
    'arch',
    'ubuntu'
]

inp_platform = prompt(PLATFORMS, 'platform')
inp_os = prompt(OS, 'os')


modules = {}

for module in os.listdir(SCRIPTS_DIR):
    module_path = path.join(SCRIPTS_DIR, module)

    if path.isdir(module_path):
        manifest_path = path.join(module_path, 'manifest.json')

        with open(manifest_path, 'r') as manifest:
            manifest = json.load(manifest)
            modules[module] = manifest

# print(json.dumps(modules, sort_keys=True, indent=4, separators=(',', ': ')))

for name, module in modules.items():
    module_path = path.join(SCRIPTS_DIR, name)

    platform = module["scripts"]["platform"][inp_platform]
    os = module["scripts"]["os"][inp_os]

    exec_scripts(platform, module_path)
    exec_scripts(os, module_path)

    


