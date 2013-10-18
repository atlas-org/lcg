# -*- python -*-
# automatically generated wscript

import waflib.Logs as msg

PACKAGE = {
    'name': 'LCG_Interfaces/ROOT',
    'author': ["ATLAS Collaboration"], 
}

def pkg_deps(ctx):
    ctx.use_pkg("LCG_Configuration")
    ctx.use_pkg("LCG_Settings")
    ctx.use_pkg("LCG_Interfaces/GCCXML")
    ctx.use_pkg("LCG_Interfaces/Python")
    ctx.use_pkg("LCG_Interfaces/xrootd")
    ctx.use_pkg("LCG_Interfaces/Qt")
    ctx.use_pkg("LCG_Interfaces/dcache_client")
    ctx.use_pkg("LCG_Interfaces/gfal")
    return

def configure(ctx):
    msg.debug('[configure] package name: '+PACKAGE['name'])
    ctx.load('find_root')
    ctx.load('find_xrootd')
    ctx.load('find_gccxml')

    macro = ctx.hwaf_declare_macro
    
    macro("ROOT_native_version", "${ROOT_config_version}")
    macro("ROOT_base", "${LCG_releases}/ROOT/${ROOT_native_version}")

    macro("ROOT_home", "${ROOT_base}/${LCG_platform}/root")

    macro("ROOTSYS", "${ROOT_home}")
    ctx.hwaf_declare_runtime_env("ROOTSYS")
    
    macro("ROOT_HOME", "${ROOT_home}")
    

    macro("ROOT_export_paths", "${ROOTSYS}")
    ctx.lcg_declare_external_package('ROOT', path='${ROOTSYS}')

    path = ctx.hwaf_subst_vars("${ROOTSYS}")
    binpath = ctx.hwaf_subst_vars("${ROOTSYS}/bin")
    ctx.find_root(path_list=[binpath], extra_paths=[path])
    
    return

def build(ctx):
    return
