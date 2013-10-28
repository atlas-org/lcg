# -*- python -*-

import waflib.Logs as msg

PACKAGE = {
    'name': 'LCG_Interfaces/GCCXML',
    'author': ["ATLAS Collaboration"], 
}

def pkg_deps(ctx):
    ctx.use_pkg("LCG_Configuration")
    ctx.use_pkg("LCG_Settings")
    return

def configure(ctx):
    msg.debug('[configure] package name: '+PACKAGE['name'])

    macro = ctx.hwaf_declare_macro
    
    macro("GCCXML_native_version", "${GCCXML_config_version}")

    macro("GCCXML_home", "${LCG_external}/gccxml/${GCCXML_native_version}/${LCG_system}")

    macro("GCCXML_name", "gccxml")

    ctx.hwaf_path_prepend('PATH', "${GCCXML_home}/bin")
    
    ctx.lcg_declare_external_package(
        "gccxml",
        path="${GCCXML_home}",
        binpath='${GCCXML_home}/bin',
        )

    ctx.load('find_gccxml')
    path_list = [ctx.hwaf_subst_vars('${GCCXML_home}/bin')]
    ctx.find_program(
        'gccxml',
        var='GCCXML',
        mandatory=True,
        path_list=path_list)
    
    return

def build(ctx):
    return
