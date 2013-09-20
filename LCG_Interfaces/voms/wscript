## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/voms",
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
    
    macro("voms_native_version", "${voms_config_version}")
    macro("voms_home", "${LCG_external}/Grid/voms/${voms_native_version}/${LCG_system}")

    macro("voms_bindir", "${voms_home}/bin")
    macro("voms_libdir", "${voms_home}/${unixdirname}")
    macro("voms_mandir", "${voms_home}/share/man")

    ctx.lcg_declare_external_package(
        'voms',
        path='${voms_home}',
        binpath='${voms_bindir}',
        libpath='${voms_libdir}',
        manpath='${voms_mandir}',
        )
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
