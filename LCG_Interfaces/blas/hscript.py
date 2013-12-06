## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/blas",
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
    
    macro("blas_native_version", "${blas_config_version}")
    macro("blas_home", "${LCG_external}/blas/${blas_native_version}/${LCG_system}")

    macro("blas_libdir", "${blas_home}/lib")
    
    macro("BLAS", "${blas_home}")
    ctx.hwaf_declare_runtime_env("BLAS")

    macro("LIB_blas", "blas")

    macro("blas_export_paths", "${blas_home}")
    ctx.lcg_declare_external_package(
        'blas',
        path='${blas_home}',
        libpath='${blas_libdir}',
        )
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{set_lib_path []})
    
    
    return # build

## EOF ##
