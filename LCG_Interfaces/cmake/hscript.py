## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/cmake",
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
    
    macro("cmake_native_version", "${cmake_config_version}")

    macro("cmake_platform", (
      {"default":    "Linux-i386"},
      {"target-mac": "Darwin"},
      {"ATLAS-pack": "${LCG_system}"},
    ))

    macro("cmake_home", "${LCG_external}/CMake/${cmake_native_version}/${cmake_platform}")
    macro("cmake_bindir", "${cmake_home}/bin")
    macro("cmake_mandir", "${cmake_home}/man")

    path = ctx.hwaf_subst_vars('${cmake_home}')
    binpath = ctx.hwaf_subst_vars('${cmake_bindir}')
    
    macro("cmake_export_paths", "${cmake_home}")
    ctx.lcg_declare_external_package(
        'cmake',
        path=path,
        binpath=binpath,
        manpath='${cmake_mandir}',
        )

    ctx.load('find_cmake')
    ctx.find_cmake(
        path_list=[binpath],
        extra_paths=[path],
        )
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{set_bin_path []})
    ##### **** statement *hlib.ApplyPatternStmt (&{set_man_path []})
    
    
    return # build

## EOF ##
