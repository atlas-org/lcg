## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/valgrind",
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
    
    macro("valgrind_native_version", "${valgrind_config_version}")

    macro("valgrind_home", "${LCG_external}/valgrind/${valgrind_native_version}/${LCG_system}")

    macro("valgrind_bindir", "${valgrind_home}/bin")
    macro("valgrind_incdir", "${valgrind_home}/include")
    macro("valgrind_libdir", "${valgrind_home}/lib/valgrind")
    
    macro("valgrind_export_paths", "${valgrind_home}")
    ctx.lcg_declare_external_package(
        'valgrind',
        path='${valgrind_home}',
        binpath='${valgrind_bindir}',
        incpath='${valgrind_incdir}',
        libpath='${valgrind_libdir}',
        )

    #ctx.hwaf_path_prepend('PKG_CONFIG_PATH', '${valgrind_home}/lib/pkgconfig')
    
    # path = ctx.hwaf_subst_vars('${valgrind_home}')
    # binpath = ctx.hwaf_subst_vars('${valgrind_bindir}')
    # ctx.load('find_valgrind')
    # ctx.find_valgrind(
    #     path_list=[binpath],
    #     extra_paths=[path],
    #     mandatory=True,
    #     )
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
