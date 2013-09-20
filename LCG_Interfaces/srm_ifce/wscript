## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/srm_ifce",
    "authors": ["ATLAS Collaboration"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Configuration", version="v*", public=True)
    ctx.use_pkg("LCG_Settings", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/lcgdmcommon", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/epel", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/Python", version="v*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    macro = ctx.hwaf_declare_macro
    
    macro("srm_ifce_native_version", "${srm_ifce_config_version}")
    macro("srm_ifce_home", "${LCG_external}/Grid/srm-ifce/${srm_ifce_native_version}/${LCG_system}")

    macro("srm_ifce_bindir", "${srm_ifce_home}/bin")
    macro("srm_ifce_incdir", "${srm_ifce_home}/include")
    macro("srm_ifce_libdir", "${srm_ifce_home}/${unixdirname}")

    macro("LIB_srm_ifce", (
      {"default": "srm-ifce"},
      {"target-win": ""},
    ))

    ctx.lcg_declare_external_package(
        'srm_ifce',
        path='${srm_ifce_home}',
        binpath='${srm_ifce_bindir}',
        incpath='${srm_ifce_incdir}',
        libpath='${srm_ifce_libdir}',
        )
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
