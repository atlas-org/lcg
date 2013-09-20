## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/gridftp_ifce",
    "authors": ["ATLAS Collaboration"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Configuration", version="v*", public=True)
    ctx.use_pkg("LCG_Settings", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/lcgdmcommon", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/Python", version="v*", public=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    macro = ctx.hwaf_declare_macro
    
    macro("gridftp_ifce_native_version", "${gridftp_ifce_config_version}")
    macro("gridftp_ifce_home", "${LCG_external}/Grid/gridftp-ifce/${gridftp_ifce_native_version}/${LCG_system}")

    macro("gridftp_ifce_bindir", "${gridftp_ifce_home}/bin")
    macro("gridftp_ifce_incdir", "${gridftp_ifce_home}/include/gridftp-ifce")
    macro("gridftp_ifce_libdir", "${gridftp_ifce_home}/${unixdirname}")
    
    macro("LIB_gridftp_ifce", (
      {"default": "gridftp-ifce"},
      {"target-win": ""},
    ))

    ctx.lcg_declare_external_package(
        'gridftp_ifce',
        path='${gridftp_ifce_home}',
        binpath='${gridftp_ifce_bindir}',
        incpath='${gridftp_ifce_incdir}',
        libpath='${gridftp_ifce_libdir}',
        )
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
