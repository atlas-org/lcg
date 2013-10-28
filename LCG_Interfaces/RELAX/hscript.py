# -*- python -*-

import waflib.Logs as msg

PACKAGE = {
    'name': 'LCG_Interfaces/RELAX',
    'author': ["ATLAS Collaboration"], 
}

def pkg_deps(ctx):
    ctx.use_pkg("LCG_Configuration")
    ctx.use_pkg("LCG_Settings")
    ctx.use_pkg("LCG_Interfaces/ROOT", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/CLHEP", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/HepMC", version="v*", public=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    macro = ctx.hwaf_declare_macro
    
    macro("RELAX_native_version", "${RELAX_config_version}")
    
    macro("RELAX_base", "${LCG_releases}/RELAX/${RELAX_native_version}")
    macro("RELAX_home", "${RELAX_base}/${LCG_platform}")

    macro("RELAX_libdir", "${RELAX_home}/lib")
    macro("RELAX_bindir", "${RELAX_home}/bin")

    ctx.hwaf_declare_macro("RELAX_export_paths", "${RELAX_libdir}")

    ctx.lcg_declare_external_package(
        "RELAX",
        path="${RELAX_home}",
        libpath="${RELAX_libdir}",
        binpath="${RELAX_bindir}",
        )
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
