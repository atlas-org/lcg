# -*- python -*-

import os.path as osp

import waflib.Logs as msg

PACKAGE = {
    'name': 'LCG_Interfaces/AIDA',
    'author': ["ATLAS Collaboration"], 
}

def pkg_deps(ctx):
    ctx.use_pkg("LCG_Configuration")
    ctx.use_pkg("LCG_Settings")
    return

def configure(ctx):
    msg.debug('[configure] package name: '+PACKAGE['name'])
    macro = ctx.hwaf_declare_macro
    
    macro("AIDA_native_version", "${AIDA_config_version}")
    macro("AIDA_home", "${LCG_external}/AIDA/${AIDA_native_version}/share")
    macro("AIDA_incdir", "${AIDA_home}/src/cpp")
    
    macro("INCLUDES_AIDA", "${AIDA_incdir}")
    
    return

def build(ctx):
    return
