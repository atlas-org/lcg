## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/pygraphics",
    "authors": ["ATLAS Collaboration"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Configuration", version="v*", public=True)
    ctx.use_pkg("LCG_Settings", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/Python", version="v*", public=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    macro = ctx.hwaf_declare_macro
    
    macro("pygraphics_native_version", "${pygraphics_config_version}_python${Python_config_version_twodigit}")

    macro("pygraphics_home", "${LCG_external}/pygraphics/${pygraphics_native_version}/${LCG_system}")

    macro("pygraphics_pydir", "${pygraphics_home}/lib/python${Python_config_version_twodigit}/site-packages")
    macro("pygraphics_bindir", "${pygraphics_home}/bin")
    macro("pygraphics_mandir", "${pygraphics_home}/share/man")
    
    macro("pyqt_resource_command", "pyrcc4")
    macro("pyqt_uic_command", (
      {"default": ["${PYTHON}", "-m", "PyQt4.uic.pyuic"]},
    ))

    ctx.hwaf_declare_macro("pygraphics_export_paths", "${pygraphics_home}")
    
    macro("pygraphics_composite_package",
          "pydot pyparsing pyqt sip")
    
    ctx.lcg_declare_external_package(
        'pygraphics',
        path='${pygraphics_home}',
        binpath='${pygraphics_bindir}',
        pypath= '${pygraphics_pydir}',
        manpath='${pygraphics_mandir}',
        )

    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    return # build

## EOF ##
