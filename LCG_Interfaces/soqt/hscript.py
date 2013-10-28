## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/soqt",
    "authors": ["ATLAS Collaboration"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Configuration", version="v*", public=True)
    ctx.use_pkg("LCG_Settings", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/Qt", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/coin3d", version="v*", public=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    macro = ctx.hwaf_declare_macro
    
    macro("soqt_native_version", "${soqt_config_version}_qt${qt_config_version}_coin3d${coin3d_config_version}")

    macro("soqt_home", "${LCG_external}/soqt/${soqt_native_version}/${LCG_system}")
    
    macro("soqt_incdir", "${soqt_home}/include")
    macro("soqt_libdir", "${soqt_home}/lib")
    macro("soqt_mandir", "${soqt_home}/share/man")
    macro("soqt_bindir", "${soqt_home}/bin")

    macro("LIB_soqt", "SoQt")
    macro("soqt_soqt-config_script", "${soqt_bindir}/soqt-config")
    
    macro("soqt_export_paths", "${soqt_home}")

    path = ctx.hwaf_subst_vars('${soqt_home}')
    binpath = ctx.hwaf_subst_vars('${soqt_bindir}')

    ctx.lcg_declare_external_package(
        'soqt',
        path=path,
        binpath='${soqt_bindir}',
        incpath='${soqt_incdir}',
        libpath='${soqt_libdir}',
        manpath='${soqt_mandir}',
        )
        
    path = ctx.hwaf_subst_vars('${soqt_home}')
    binpath = ctx.hwaf_subst_vars('${soqt_bindir}')
    
    kwargs = {
        'path_list': binpath,
        'extra_paths': path,
        }
    ctx.find_program(
        'soqt-config', 
        var='SOQT-CONFIG',
        **kwargs)
    soqt_cfg = ctx.env['SOQT-CONFIG']

    ctx.check_with(
        ctx.check_cfg,
        "soqt",
        path=soqt_cfg,
        package="",
        uselib_store="soqt",
        args='--libs',
        **kwargs)
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
