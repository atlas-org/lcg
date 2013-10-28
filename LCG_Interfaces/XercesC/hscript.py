## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/XercesC",
    "authors": ["ATLAS Collaboration"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Configuration", version="v*", public=True)
    ctx.use_pkg("LCG_Settings", version="v*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    macro = ctx.hwaf_declare_macro

    macro("XercesC_native_version", "${XercesC_config_version}")

    macro("XercesC_home", "${LCG_external}/XercesC/${XercesC_native_version}/${LCG_system}")

    macro("XercesC_incdir", "${XercesC_home}/include")
    macro("XercesC_libdir", "${XercesC_home}/lib")
    
    macro("LIB_XercesC", (
      {"default": ["xerces-c", "pthread"]},
      {"target-win": "xerces-c_3"},
    ))

    ctx.hwaf_macro_append("CXXFLAGS_XercesC", (
      {"default": ""},
      {"target-linux": ["-w", "-Wno-unused"]},
    ))
    
    ctx.hwaf_macro_append("DEFINES_XercesC", "XERCESC_GE_31")
    
    macro("XercesC_export_paths", (
      {"default": ["${XercesC_incdir}", "${XercesC_libdir}"]},
    ))

    ctx.lcg_declare_external_package(
        'XercesC',
        path="${XercesC_home}",
        incpath="${XercesC_incdir}",
        libpath="${XercesC_libdir}",
        )
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
