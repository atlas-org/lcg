## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/HepMC",
    "authors": ["ATLAS Collaboration"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Configuration", version="v*", public=True)
    ctx.use_pkg("LCG_Settings", version="v*", public=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    macro = ctx.hwaf_declare_macro
    
    macro("HepMC_native_version", "${HepMC_config_version}")
    macro("HepMC_home", "${LCG_external}/HepMC/${HepMC_native_version}/${LCG_system}")
    
    macro("HepMC_incdir", "${HepMC_home}/include")
    macro("HepMC_libdir", "${HepMC_home}/lib")

    macro("LIB_HepMC", "HepMC")

    macro("HepMC_export_paths", (
      {"default": ["${HepMC_incdir}", "${HepMC_libdir}"]},
      {"ATLAS": ""},
    ))

    ctx.lcg_declare_external_package(
        'HepMC',
        path='${HepMC_home}',
        incpath='${HepMC_incdir}',
        libpath='${HepMC_libdir}',
        )
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
