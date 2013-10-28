## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/qwt",
    "authors": ["ATLAS Collaboration"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Configuration", version="v*", public=True)
    ctx.use_pkg("LCG_Settings", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/Qt", version="v*", public=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    macro = ctx.hwaf_declare_macro
    
    macro("qwt_native_version", "${qwt_config_version}_qt${qt_config_version}")
    macro("qwt_home", "${LCG_external}/qwt/${qwt_native_version}/${LCG_system}")
    
    macro("qwt_incdir", "${qwt_home}/include")
    macro("qwt_libdir", "${qwt_home}/lib")
    macro("qwt_mandir", "${qwt_home}/share/man")

    macro("LIB_qwt", "qwt")
    macro("LIB_qwtmathml", (
        {"default": ["qwt", "qwtmathml"]},
    ))
    
    macro("qwt_export_paths", "${qwt_home}")

    ctx.lcg_declare_external_package(
        'qwt',
        path='${qwt_home}',
        incpath='${qwt_incdir}',
        libpath='${qwt_libdir}',
        manpath='${qwt_mandir}',
        )
        
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
