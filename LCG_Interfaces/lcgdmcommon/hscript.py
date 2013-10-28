## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/lcgdmcommon",
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
    
    macro("lcgdmcommon_native_version", "${lcgdmcommon_config_version}")
    macro("lcgdmcommon_home", "${LCG_external}/Grid/lcg-dm-common/${lcgdmcommon_native_version}/${LCG_system}")

    macro("lcgdmcommon_libdir", "${lcgdmcommon_home}/${unixdirname}")

    macro("lcgdmcommon_export_paths", "${lcgdmcommon_libdir}")

    ctx.lcg_declare_external_package(
        'lcgdmcommon',
        path='${lcgdmcommon_home}',
        libpath='${lcgdmcommon_libdir}',
        )
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
