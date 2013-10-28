## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/pytools",
    "authors": ["ATLAS Collaboration"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Configuration", version="v*", public=True)
    ctx.use_pkg("LCG_Settings", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/Python", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/mysql", version="v*", public=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    macro = ctx.hwaf_declare_macro
    
    macro("pytools_native_version", "${pytools_config_version}_python${Python_config_version_twodigit}")
    macro("pytools_home", "${LCG_external}/pytools/${pytools_native_version}/${LCG_system}")
    macro("pytools_bindir", "${pytools_home}/bin")
    macro("pytools_pydir", "${pytools_home}/lib/python${Python_config_version_twodigit}/site-packages")

    macro("pytools_export_paths", "${pytools_home}")

    macro("pytools_composite_package",
          "4suite cx_oracle ipython json mock mysql_python processing py pyxml setuptools storm")
    
    ctx.lcg_declare_external_package(
        'pytools',
        path='${pytools_home}',
        binpath='${pytools_bindir}',
        pypath= '${pytools_pydir}',
        )
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    return # build

## EOF ##
