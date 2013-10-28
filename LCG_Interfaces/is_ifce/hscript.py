## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/is_ifce",
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
    
    macro("is_ifce_native_version", "${is_ifce_config_version}")
    macro("is_ifce_home", "${LCG_external}/Grid/is-ifce/${is_ifce_native_version}/${LCG_system}")

    macro("is_ifce_bindir", "${is_ifce_home}/bin")
    macro("is_ifce_incdir", "${is_ifce_home}/include")
    macro("is_ifce_libdir", "${is_ifce_home}/${unixdirname}")

    macro("LIB_is_ifce", (
      {"default": "is-ifce"},
      {"target-win": ""},
    ))

    ctx.lcg_declare_external_package(
        'is_ifce',
        path='${is_ifce_home}',
        binpath='${is_ifce_bindir}',
        incpath='${is_ifce_incdir}',
        libpath='${is_ifce_libdir}',
        )
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
