## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/dpm",
    "authors": ["ATLAS Collaboration"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Configuration", version="v*", public=True)
    ctx.use_pkg("LCG_Settings", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/lcgdmcommon", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/Python", version="v*", public=True)
    
    ## no private dependencies
    ## runtime dependencies
    ctx.use_pkg("LCG_Interfaces/Python", version="v*", runtime=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    macro = ctx.hwaf_declare_macro
    
    macro("dpm_native_version", "${dpm_config_version}")

    macro("dpm_path", "Grid/DPM")

    macro("dpm_home", "${LCG_external}/${dpm_path}/${dpm_native_version}/${LCG_system}")

    macro("dpm_bindir", "${dpm_home}/bin")
    macro("dpm_incdir", "${dpm_home}/include")
    macro("dpm_libdir", "${dpm_home}/${unixdirname}")
    macro("dpm_mandir", "${dpm_home}/share/man")
    macro("dpm_pydir",  "${dpm_home}/${unixdirname}/python${Python_config_version_twodigit}")

    ctx.hwaf_path_prepend("LD_LIBRARY_PATH", (
      {"default": "${dpm_home}/${unixdirname}"},
      {"target-win": ""},
      {"noDPM": ""},
    ))
    
    ctx.hwaf_path_prepend("PYTHONPATH", "${dpm_pydir}")
    
    macro("LIB_dpm", (
      {"default": "dpm"},
      {"target-win": ""},
    ))
    
    ctx.lcg_declare_external_package(
        'dpm',
        path='${dpm_home}',
        binpath='${dpm_bindir}',
        incpath='${dpm_incdir}',
        libpath='${dpm_libdir}',
        manpath='${dpm_mandir}',
        pypath= '${dpm_pydir}',
        )

    macro("dpm_export_paths", (
      {"default": ["${dpm_incdir}", "${dpm_bindir}", "${dpm_libdir}", "${dpm_mandir}"]},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
