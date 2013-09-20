## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/gfal",
    "authors": ["ATLAS Collaboration"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Configuration", version="v*", public=True)
    ctx.use_pkg("LCG_Settings", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/lfc", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/gridftp_ifce", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/srm_ifce", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/is_ifce", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/voms", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/libtool", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/epel", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/Python", version="v*", public=True)
    
    ## no private dependencies
    ## runtime dependencies
    ctx.use_pkg("LCG_Interfaces/Python", version="v*", runtime=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    macro = ctx.hwaf_declare_macro
    
    macro("gfal_native_version", "${gfal_config_version}")
    macro("gfal_home", "${LCG_external}/Grid/gfal/${gfal_native_version}/${LCG_system}")

    macro("gfal_bindir", "${gfal_home}/bin")
    macro("gfal_incdir", "${gfal_home}/include")
    macro("gfal_libdir", "${gfal_home}/${unixdirname}")
    macro("gfal_mandir", "${gfal_home}/share/man")
    macro("gfal_pydir",  "${gfal_home}/${unixdirname}/python${Python_config_version_twodigit}/site-packages")

    macro("LIB_gfal", (
      {"default":    "gfal"},
      {"target-win": ""},
    ))
    
    macro("LIBPATH_gfal", (
      {"default": ["${gfal_libdir}", "${epel_libdir}", "${lfc_libdir}"]},
      {"target-win": ""},
    ))

    ctx.lcg_declare_external_package(
        "gfal",
        path='${gfal_home}',
        binpath='${gfal_bindir}',
        incpath='${gfal_incdir}',
        libpath='${gfal_libdir}',
        manpath='${gfal_mandir}',
        pypath ='${gfal_pydir}',
        )
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
