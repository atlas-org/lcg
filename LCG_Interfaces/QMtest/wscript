## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/QMtest",
    "authors": ["ATLAS Collaboration"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Configuration", version="v*", public=True)
    ctx.use_pkg("LCG_Settings", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/Python", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/CppUnit", version="v*", public=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    macro = ctx.hwaf_declare_macro
    
    macro("QMtest_native_version", "${QMtest_config_version}_python${Python_config_version_twodigit}")
    
    macro("QMtest_home", "${LCG_external}/QMtest/${QMtest_native_version}/${LCG_system}")
    macro("QM_home", "${QMtest_home}")
    ctx.hwaf_declare_runtime_env("QM_home")

    macro("QMtest_bindir", "${QMtest_home}/bin")
    macro("QMtest_pydir",  (
        {"default":"${QMtest_home}/lib/python${Python_config_version_twodigit}/site-packages"},
        {"target-win":"${QMtest_home}\\Lib\\site-packages"},
    ))
    macro("QMtest_mandir", "${QMtest_home}/share/man")
    
    ctx.hwaf_path_prepend("PATH", (
      {"default": "${QMtest_bindir}"},
      {"target-win": "${QMtest_home}\\Scripts;${QMtest_home}\\Lib\\site-packages\\pywin32_system32"},
    ))

    ctx.hwaf_declare_macro("QMtest_export_paths", (
      {"default": "${QMtest_home}"},
    ))

    ctx.lcg_declare_external_package(
        "QMtest",
        path="${QMtest_home}",
        binpath="${QMtest_bindir}",
        pypath ="${QMtest_pydir}",
        manpath="${QMtest_mandir}",
        )
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
