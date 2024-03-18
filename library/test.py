#!/usr/bin/python3
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule

def presentation(module):
	name = module.params['name']
	attack = module.params['attack']
	inventory = module.params['inventory']
	return {"Presentation" : "My name is {} and my type of attack is {}, here is what you will find in my inventory : {}".format(name, attack, inventory)}

def main():

	fields = {
		"name": {"default" : "unknown", "type": "str"},
		"description": {"default": "empty", "required": False, "type": "str"},
        "attack": {
        	"default": "melee",
        	"choices": ['melee', 'distance'],
        	"type": 'str'
        },
		"inventory": {"default": [], "required": False, "type": "list"},
		"monster": {"default": False, "required": False, "type": "bool"},
	}
	module = AnsibleModule(argument_spec=fields)
	#module.exit_json(changed=False, meta=module.params)
	module.exit_json(changed=False, meta=presentation(module))

if __name__ == '__main__':
    main()
