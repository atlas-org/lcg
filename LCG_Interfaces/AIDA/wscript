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
    ctx.hwaf_declare_macro("AIDA_native_version", (
        {"default": "${AIDA_config_version}"},
    ))
    ctx.hwaf_declare_macro("AIDA_home", (
        {"default": "${LCG_external}/AIDA/${AIDA_native_version}/share"},
    ))
    return

def build(ctx):
    incdir = 'inc'
    incdir_node = ctx.path.find_dir(incdir)
    if not incdir_node:
        ctx.fatal('no such directory [%s]' % incdir)
        pass
    includes = incdir_node.ant_glob('**/*', dir=False)

    prefix = osp.join('${INSTALL_AREA}',
                      'include',
                      'AIDA',
                      )
    relative_trick=False
    
    ctx.install_files(
        prefix,
        includes,
        relative_trick=relative_trick,
        cwd=None,
        )
    return
