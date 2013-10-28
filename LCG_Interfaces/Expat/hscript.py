## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/Expat",
    "authors": ["ATLAS Collaboration"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Configuration", version="v*", public=True)
    ctx.use_pkg("LCG_Settings", version="v*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    macro = ctx.hwaf_declare_macro
    
    macro("Expat_native_version", "${Expat_config_version}")
    macro("Expat_home", "${LCG_external}/expat/${Expat_native_version}/${LCG_system}")

    macro("Expat_incdir", "${Expat_home}/include")
    macro("Expat_libdir", (
        {"default":    "${Expat_home}/lib"},
        {"target-win": "${Expat_home}/Libs"},
    ))
    
    macro("LIB_Expat", "expat")

    macro("Expat_name", "expat")

    ctx.hwaf_declare_macro("Expat_export_paths", (
      {"default": ["${Expat_libdir}", "${Expat_incdir}"]},
    ))

    ctx.lcg_declare_external_package(
        "Expat",
        path="${Expat_home}",
        incpath="${Expat_incdir}",
        libpath="${Expat_libdir}",
        )
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
