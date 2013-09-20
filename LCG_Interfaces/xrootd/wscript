# -*- python -*-

import waflib.Logs as msg

PACKAGE = {
    'name': 'LCG_Interfaces/xrootd',
    'author': ["ATLAS Collaboration"], 
}

def pkg_deps(ctx):
    ctx.use_pkg("LCG_Configuration")
    ctx.use_pkg("LCG_Settings")
    return

def configure(ctx):
    msg.debug('[configure] package name: '+PACKAGE['name'])

    macro = ctx.hwaf_declare_macro
    
    macro("xrootd_native_version", "${xrootd_config_version}")
    macro("xrootd_home", "${LCG_external}/xrootd/${xrootd_native_version}/${LCG_system}")

    macro("xrootd_bindir", "${xrootd_home}/bin")
    macro("xrootd_incdir", "${xrootd_home}/include")
    macro("xrootd_libdir", "${xrootd_home}/${unixdirname}")
    
    ctx.lcg_declare_external_package(
        'xrootd',
        path='${xrootd_home}',
        binpath='${xrootd_bindir}',
        incpath='${xrootd_incdir}',
        libpath='${xrootd_libdir}',
        )
    return

def build(ctx):
    return
