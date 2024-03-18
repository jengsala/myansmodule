#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule


def verifyAge(module):
    age = module.params["age"]
    if age < 18:
        module.fail_json(
            msg="Attention vous êtes mineur, un accord parental est requis."
        )


def main():
    fields = {"age": {"type": "int"}}
    module = AnsibleModule(argument_spec=fields)
    verifyAge(module)
    module.exit_json(changed=False, meta=module.params["age"])


if __name__ == "__main__":
    main()
