#!/usr/bin/python3
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule

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
	module.exit_json(changed=False, meta=module.params)


if __name__ == '__main__':
    main()
