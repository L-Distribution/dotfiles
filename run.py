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
		print("Select a %s:" % type_name)

		for index, entry in enumerate(consts):
			print("[%i] %s" % (index + 1, entry))

		try: 
			res = consts[int(input("> ")) - 1]
			print("[I] Selected %s: %s" % (type_name, res))
		except KeyboardInterrupt:
			sys.exit()
		except: 
			print("[E] Invalid input!\n")
		

	return res
	

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
	# subprocess.call([ name ])
	print(module)

        platform = module["scripts"]["platform"][inp_platform]
        print(platformat)
