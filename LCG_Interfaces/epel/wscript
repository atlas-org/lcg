## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/epel",
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
    
    macro("epel_native_version", "${epel_config_version}")
    macro("epel_home", "${LCG_external}/Grid/epel/${epel_native_version}/${LCG_system}")

    macro("epel_bindir", "${epel_home}/bin")
    macro("epel_libdir", "${epel_home}/${unixdirname}")

    macro("epel_export_paths", (
        {"default": ["${epel_libdir}", "${epel_bindir}"]},
    ))
    
    ctx.lcg_declare_external_package(
        'epel',
        path='${epel_home}',
        libpath='${epel_libdir}',
        binpath='${epel_bindir}',
        )
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
