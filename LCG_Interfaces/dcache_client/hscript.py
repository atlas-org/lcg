## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/dcache_client",
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
    
    macro("dcache_client_native_version", "${dcache_client_config_version}")

    macro("dcache_client_home", (
      {"default": "${LCG_external}/dcache_client/${dcache_client_native_version}/${LCG_system}"},
      {"target-win": ""},
    ))

    macro("dcache_client_bindir", "${dcache_client_home}/dcap/bin")
    macro("dcache_client_incdir", "${dcache_client_home}/dcap/include")
    macro("dcache_client_libdir", "${dcache_client_home}/dcap/${unixdirname}")

    macro("SRM_PATH", "${dcache_client_home}/srm")
    ctx.hwaf_declare_runtime_env("SRM_PATH")
    
    macro("LIB_dcache_client", (
      {"default": "dcap"},
      {"target-win": ""},
    ))
    
    macro("dcache_client_name", "dcache_client")

    ctx.hwaf_path_prepend("PATH", (
      {"default": "${SRM_PATH}/bin"},
      {"target-win": ""},
    ))

    macro("dcache_client_export_paths", (
      {"default": ["${dcache_client_incdir}", "${dcache_client_libdir}"]},
    ))

    ctx.lcg_declare_external_package(
        'dcache_client',
        path='${dcache_client_home}',
        binpath='${dcache_client_bindir}',
        incpath='${dcache_client_incdir}',
        libpath='${dcache_client_libdir}',
        )
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
