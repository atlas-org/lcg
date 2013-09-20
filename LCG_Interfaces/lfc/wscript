## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/lfc",
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
    
    macro("lfc_native_version", "${lfc_config_version}")
    macro("lfc_home", "${LCG_external}/Grid/LFC/${lfc_native_version}/${LCG_system}")

    macro("lfc_bindir", "${lfc_home}/bin")
    macro("lfc_incdir", "${lfc_home}/include/lfc")
    macro("lfc_libdir", "${lfc_home}/${unixdirname}")
    macro("lfc_pydir",  "${lfc_home}/${unixdirname}/python${Python_config_version_twodigit}/site-packages")

    ctx.hwaf_path_prepend('PYTHONPATH', (
        {"default": "${lfc_pydir}"},
        {"target-win": ""},
    ))

    macro("LIB_lfc", "lfc")

    ctx.lcg_declare_external_package(
        'lfc',
        path='${lfc_home}',
        binpath='${lfc_bindir}',
        incpath='${lfc_incdir}',
        libpath='${lfc_libdir}',
        pypath='${lfc_pydir}',
        )
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{set_ext_bin_and_lib_path [windir=lib unixdir=$(unixdirname)]})
    ##### **** statement *hlib.ApplyPatternStmt (&{set_ext_man_path [mandir="share/man]})
    
    
    return # build

## EOF ##
