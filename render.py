#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
from jinja2 import Environment, FileSystemLoader

def get_tex_tpl(path):
    texenv = Environment(loader=FileSystemLoader(os.getcwd()))
    texenv.block_start_string = '((*'
    texenv.block_end_string = '*))'
    texenv.variable_start_string = '((('
    texenv.variable_end_string = ')))'
    texenv.comment_start_string = '((='
    texenv.comment_end_string = '=))'
    texenv.trim_blocks = True
    texenv.lstrip_blocks = True

    return texenv.get_template(path)

def get_conf(module):
    conf = {}
    for k in dir(module):
        if k.startswith("_"): continue
        conf[k] = getattr(module, k)
    return conf


if __name__ == "__main__":
    import config

    print(get_tex_tpl(sys.argv[1])
          .render(get_conf(config))
          .encode('utf-8'))
