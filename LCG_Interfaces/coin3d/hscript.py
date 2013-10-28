## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/coin3d",
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
    
    macro("coin3d_native_version", "${coin3d_config_version}")
    macro("coin3d_home", "${LCG_external}/coin3d/${coin3d_native_version}/${LCG_system}")

    macro("coin3d_incdir", "${coin3d_home}/include")
    macro("coin3d_libdir", "${coin3d_home}/lib")
    macro("coin3d_bindir", "${coin3d_home}/bin")
    macro("coin3d_mandir", "${coin3d_home}/share/man")

    macro("LIB_coin3d", "Coin")
    macro("coin3d_coin-config_script", "${coin3d_bindir}/coin-config")
    
    macro("coin3d_export_paths", (
      {"default": ["${coin3d_incdir}", "${coin3d_libdir}", "${coin3d_bindir}"]},
    ))

    ctx.lcg_declare_external_package(
        'coin3d',
        path='${coin3d_home}',
        binpath='${coin3d_bindir}',
        incpath='${coin3d_incdir}',
        libpath='${coin3d_libdir}',
        )

    path = ctx.hwaf_subst_vars('${coin3d_home}')
    binpath = ctx.hwaf_subst_vars('${coin3d_bindir}')
    
    kwargs = {
        'path_list': binpath,
        'extra_paths': path,
        }
    ctx.find_program(
        'coin-config', 
        var='COIN-CONFIG',
        **kwargs)
    coin_cfg = ctx.env['COIN-CONFIG']

    ctx.check_with(
        ctx.check_cfg,
        "coin3d",
        path=coin_cfg,
        package="",
        uselib_store="coin3d",
        args='--libs',
        **kwargs)
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
