## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/sqlite",
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
    
    macro("sqlite_native_version", "${sqlite_config_version}")

    macro("sqlite_home", "${LCG_external}/sqlite/${sqlite_native_version}/${LCG_system}")

    macro("sqlite_bindir", "${sqlite_home}/bin")
    macro("sqlite_incdir", "${sqlite_home}/include")
    macro("sqlite_libdir", "${sqlite_home}/lib")
    

    macro("sqlite_export_paths", (
      {"default": ["${sqlite_incdir}", "${sqlite_libdir}", "${sqlite_bindir}"]},
    ))

    macro("LIB_sqlite", "sqlite3")

    ctx.lcg_declare_external_package(
        'sqlite',
        path='${sqlite_home}',
        binpath='${sqlite_bindir}',
        incpath='${sqlite_incdir}',
        libpath='${sqlite_libdir}',
        )

    ctx.load('find_sqlite')
    path=ctx.hwaf_subst_vars('${sqlite_home}')
    binpath=ctx.hwaf_subst_vars('${sqlite_bindir}')
    ctx.find_sqlite(
        path_list=[binpath],
        extra_paths=[path],
        )
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{set_bin_and_lib_path []})
    
    
    return # build

## EOF ##
