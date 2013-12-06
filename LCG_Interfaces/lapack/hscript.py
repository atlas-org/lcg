## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/lapack",
    "authors": ["ATLAS Collaboration"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Configuration", version="v*", public=True)
    ctx.use_pkg("LCG_Settings", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/blas", version="v*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    macro = ctx.hwaf_declare_macro
    
    macro("lapack_native_version", "${lapack_config_version}")
    macro("lapack_home", "${LCG_external}/lapack/${lapack_native_version}/${LCG_system}")

    macro("lapack_libdir", "${lapack_home}/lib")
    
    macro("LAPACK", "${lapack_home}")

    macro("LIB_lapack", (
      {"default": "LAPACK"},
      {"target-win": "lapack3"},
    ))

    macro("lapack_export_paths", "${lapack_home}")
    ctx.lcg_declare_external_package(
        'lapack',
        path='${lapack_home}',
        libpath='${lapack_libdir}',
        )
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{set_lib_path []})
    
    
    return # build

## EOF ##
