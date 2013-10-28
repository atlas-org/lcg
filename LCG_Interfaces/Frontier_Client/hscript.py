## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/Frontier_Client",
    "authors": ["ATLAS Collaboration"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Configuration", version="v*", public=True)
    ctx.use_pkg("LCG_Settings", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/Expat", version="v*", public=True)
    
    ## no private dependencies
    ## runtime dependencies
    ctx.use_pkg("LCG_Interfaces/Expat", version="v*", runtime=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    macro = ctx.hwaf_declare_macro
    
    macro("Frontier_Client_native_version", "${Frontier_Client_config_version}")
    macro("Frontier_Client_home", "${LCG_external}/frontier_client/${Frontier_Client_native_version}/${LCG_system}")

    macro("Frontier_Client_bindir", "${Frontier_Client_home}/bin")
    macro("Frontier_Client_incdir", "${Frontier_Client_home}/include")
    macro("Frontier_Client_libdir", "${Frontier_Client_home}/lib")

    macro("LIB_Frontier_Client", "frontier_client")

    macro("Frontier_Client_name", "frontier_client")

    macro("Frontier_Client_export_paths", (
      {"default": ["${Frontier_Client_bindir}",
                   "${Frontier_Client_libdir}",
                   "${Frontier_Client_incdir}"]},
    ))

    ctx.lcg_declare_external_package(
        'Frontier_Client',
        path='${Frontier_Client_home}',
        binpath='${Frontier_Client_bindir}',
        incpath='${Frontier_Client_incdir}',
        libpath='${Frontier_Client_libdir}',
        )
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
