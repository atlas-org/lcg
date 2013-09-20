## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/pyanalysis",
    "authors": ["ATLAS Collaboration"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Configuration", version="v*", public=True)
    ctx.use_pkg("LCG_Settings", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/Python", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/blas", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/lapack", version="v*", public=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    macro = ctx.hwaf_declare_macro
    
    macro("pyanalysis_native_version", "${pyanalysis_config_version}_python${Python_config_version_twodigit}")

    macro("pyanalysis_home", "${LCG_external}/pyanalysis/${pyanalysis_native_version}/${LCG_system}")
    
    macro("pyanalysis_bindir", "${pyanalysis_home}/bin")
    macro("pyanalysis_pydir",  "${pyanalysis_home}/lib/python${Python_config_version_twodigit}/site-packages")
    macro("pyanalysis_mandir", "${pyanalysis_home}/share/man")

    macro("pyanalysis_export_paths", "${pyanalysis_home}")

    macro("pyanalysis_composite_package", "matplotlib numpy scipy")
    
    ctx.lcg_declare_external_package(
        'pyanalysis',
        path='${pyanalysis_home}',
        binpath='${pyanalysis_bindir}',
        pypath= '${pyanalysis_pydir}',
        manpath='${pyanalysis_mandir}',
        )

    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    return # build

## EOF ##
