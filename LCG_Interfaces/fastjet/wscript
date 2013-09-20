## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/fastjet",
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
    
    macro("fastjet_native_version", "${fastjet_config_version}")
    macro("fastjet_home", "${LCG_external}/fastjet/${fastjet_native_version}/${LCG_system}")

    macro("fastjet_incdir", "${fastjet_home}/include")
    macro("fastjet_libdir", "${fastjet_home}/lib")
    macro("fastjet_bindir", "${fastjet_home}/bin")

    macro("LIB_fastjet", (
        {"default": ["fastjet", "fastjettools"]},
    ))

    macro("fastjet_export_paths", (
      {"default": ["${fastjet_incdir}", "${fastjet_libdir}"]},
    ))

    ctx.lcg_declare_external_package(
        'fastjet',
        path='${fastjet_home}',
        binpath='${fastjet_bindir}',
        incpath='${fastjet_incdir}',
        libpath='${fastjet_libdir}',
        )
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
