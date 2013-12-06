## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/libtool",
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
    
    macro("libtool_native_version", "${libtool_config_version}")
    macro("libtool_home", "${LCG_external}/libtool/${libtool_native_version}/${LCG_system}")

    macro("libtool_bindir", "${libtool_home}/bin")
    macro("libtool_incdir", "${libtool_home}/include")
    macro("libtool_libdir", "${libtool_home}/lib")
    macro("libtool_mandir", "${libtool_home}/share/man")

    macro("LIB_libtool", (
      {"default": "ltdl"},
      {"target-win": ""},
    ))

    macro("libtool_export_paths", "${libtool_home}")
    ctx.lcg_declare_external_package(
        'libtool',
        path='${libtool_home}',
        binpath='${libtool_bindir}',
        incpath='${libtool_incdir}',
        libpath='${libtool_libdir}',
        manpath='${libtool_mandir}',
        )
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
