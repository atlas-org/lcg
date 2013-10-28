## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/mysql",
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
    
    macro("mysql_native_version", "${mysql_config_version}")
    macro("mysql_home", "${LCG_external}/mysql/${mysql_native_version}/${LCG_system}")

    macro("mysql_bindir", "${mysql_home}/bin")
    macro("mysql_incdir", "${mysql_home}/include")
    macro("mysql_libdir", "${mysql_home}/lib")
    macro("mysql_mandir", "${mysql_home}/man")
    
    macro("LIB_mysql", (
        {"default":    "mysqlclient_r"},
        {"target-win": "mysql"},
    ))
    
    ctx.hwaf_path_append("PATH", (
      {"target-win": "${mysql_libdir}"},
    ))
    
    ctx.hwaf_declare_macro("mysql_export_paths", (
      {"default": ["${mysql_incdir}", "${mysql_libdir}"]},
    ))

    ctx.lcg_declare_external_package(
        'mysql',
        path='${mysql_home}',
        binpath='${mysql_bindir}',
        incpath='${mysql_incdir}',
        libpath='${mysql_libdir}',
        manpath='${mysql_mandir}',
        )
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
