## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/HepPDT",
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
    
    macro("HepPDT_native_version", "${HepPDT_config_version}")
    macro("HepPDT_home", "${LCG_external}/HepPDT/${HepPDT_native_version}/${LCG_system}")

    macro("HepPDT_incdir", "${HepPDT_home}/include")
    macro("HepPDT_libdir", "${HepPDT_home}/lib")

    macro("LIB_HepPDT", (
      {"default": ["HepPDT", "HepPID"]},
    ))

    macro("HepPDT_export_paths", (
      {"default": ["${HepPDT_incdir}", "${HepPDT_libdir}"]},
    ))

    ctx.lcg_declare_external_package(
        'HepPDT',
        path='${HepPDT_home}',
        incpath='${HepPDT_incdir}',
        libpath='${HepPDT_libdir}',
        )
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{set_lib_path []})
    
    
    return # build

## EOF ##
