## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/COOL",
    "authors": ["ATLAS Collaboration"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Configuration", version="v*", public=True)
    ctx.use_pkg("LCG_Settings", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/CORAL", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/Python", version="v*", public=True)

    # optional
    ctx.use_pkg("LCG_Interfaces/Qt")
    ctx.use_pkg("LCG_Interfaces/Reflex")

    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    macro = ctx.hwaf_declare_macro
    
    macro("COOL_native_version", "${COOL_config_version}")
    macro("COOL_base", "${LCG_releases}/COOL/${COOL_native_version}")

    macro("COOL_home", "${COOL_base}/${LCG_platform}")

    macro("COOL_bindir", "${COOL_home}/bin")
    macro("COOL_incdir", "${COOL_base}/include")
    macro("COOL_libdir", "${COOL_home}/lib")
    macro("COOL_pydir",  "${COOL_home}/python")

    ctx.hwaf_declare_tag("NEEDS_COOL_FACTORY", content=[])
    ctx.hwaf_declare_tag("NEEDS_PYCOOL",       content=[])
    
    macro("LIB_COOL", (
        {"default": "lcg_CoolKernel"},
        {"NEEDS_COOL_FACTORY": ["lcg_CoolKernel", "lcg_CoolApplication"]},
    ))
    
    macro("COOL_export_paths", (
      {"default": ["${COOL_home}/bin", "${COOL_home}/lib", "${COOL_home}/tests", "${COOL_base}/include", "${COOL_home}/python"]},
    ))

    ctx.hwaf_path_prepend("PYTHONPATH", (
      {"default": ""},
      {("NEEDS_PYCOOL", "target-win"): "${COOL_home}\\python"},
      {"NEEDS_PYCOOL": "${COOL_home}/python"},
    ))

    ctx.lcg_declare_external_package(
        'COOL',
        path='${COOL_home}',
        incpath='${COOL_incdir}',
        libpath='${COOL_libdir}',
        binpath='${COOL_bindir}',
        )
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##