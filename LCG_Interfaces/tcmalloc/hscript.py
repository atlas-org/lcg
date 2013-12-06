## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/tcmalloc",
    "authors": ["ATLAS Collaboration"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Configuration", version="v*", public=True)
    ctx.use_pkg("LCG_Settings", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/libunwind", version="v*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    macro = ctx.hwaf_declare_macro
    
    macro("tcmalloc_native_version", "${tcmalloc_config_version}")
    macro("tcmalloc_home", "${LCG_external}/tcmalloc/${tcmalloc_native_version}/${LCG_system}")

    #macro("tcmalloc_bindir", "${tcmalloc_home}/bin")
    macro("tcmalloc_incdir", "${tcmalloc_home}/include")
    macro("tcmalloc_libdir", "${tcmalloc_home}/lib")
    macro("tcmalloc_mandir", "${tcmalloc_home}/share/man")

    macro("tcmalloc_export_paths", "${tcmalloc_home}")
    ctx.lcg_declare_external_package(
        'tcmalloc',
        path='${tcmalloc_home}',
        #binpath='${tcmalloc_bindir}',
        incpath='${tcmalloc_incdir}',
        libpath='${tcmalloc_libdir}',
        #pypath='${tcmalloc_pydir}',
        manpath='${tcmalloc_mandir}',
        )

    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    return # build

## EOF ##
