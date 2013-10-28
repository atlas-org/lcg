## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/tbb",
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
    
    macro("tbb_native_version", "${tbb_config_version}")
    macro("tbb_home", "${LCG_external}/tbb/${tbb_native_version}/${LCG_system}")

    macro("tbb_incdir", "${tbb_home}/include")
    macro("tbb_libdir", "${tbb_home}/bin") # yes. /bin

    macro("LIB_tbb", "tbb")

    macro("tbb_export_paths", (
      {"default": ["${tbb_incdir}", "${tbb_libdir}"]},
    ))

    ctx.lcg_declare_external_package(
        'tbb',
        path='${tbb_home}',
        libpath='${tbb_libdir}',
        incpath='${tbb_incdir}',
        )

    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{set_ext_bin_and_lib_path [unixdir=bin]})
    
    
    return # build

## EOF ##
