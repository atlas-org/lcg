## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/GSL",
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
    
    macro("GSL_native_version", "${GSL_config_version}")
    macro("GSL_home", "${LCG_external}/GSL/${GSL_native_version}/${LCG_system}")

    macro("GSL_bindir", "${GSL_home}/bin")
    macro("GSL_incdir", "${GSL_home}/include")
    macro("GSL_libdir", "${GSL_home}/lib")
    macro("GSL_mandir", "${GSL_home}/share/man")

    macro("LIB_GSL", ({"default": ["gsl", "gslcblas"]},))
    
    ctx.hwaf_macro_append("DEFINES_GSL", (
      {"default": ""},
      {"target-win": "GSL_DLL"},
    ))
    
    ctx.hwaf_declare_macro("GSL_export_paths", (
      {"default": ["${GSL_libdir}", "${GSL_incdir}", "${GSL_bindir}"]},
    ))

    ctx.lcg_declare_external_package(
        'GSL',
        path='${GSL_home}',
        binpath='${GSL_bindir}',
        incpath='${GSL_incdir}',
        libpath='${GSL_libdir}',
        manpath='${GSL_mandir}',
        )
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
