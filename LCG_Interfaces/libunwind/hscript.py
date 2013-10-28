## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/libunwind",
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
    
    macro("libunwind_native_version", "${libunwind_config_version}")
    macro("libunwind_home", "${LCG_external}/libunwind/${libunwind_native_version}/${LCG_system}")

    macro("libunwind_incdir", "${libunwind_home}/include")
    macro("libunwind_libdir", "${libunwind_home}/lib")
    macro("libunwind_mandir", "${libunwind_home}/man")
    
    macro("LIB_libunwind", (
      {"default": ["unwind", "unwind-x86"]},
      {"target-x86_64": ["unwind", "unwind-x86_64"]},
    ))
    
    macro("libunwind_export_paths", (
      {"default": ["${libunwind_incdir}", "${libunwind_libdir}"]},
    ))

    ctx.lcg_declare_external_package(
        'libunwind',
        path='${libunwind_home}',
        incpath='${libunwind_incdir}',
        libpath='${libunwind_libdir}',
        manpath='${libunwind_mandir}',
        )
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
