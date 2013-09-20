## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/oracle",
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
    
    macro("oracle_native_version", "${oracle_config_version}")

    macro("oracle_home", "${LCG_external}/oracle/${oracle_native_version}/${LCG_system}")

    macro("oracle_bindir", "${oracle_home}/bin")
    macro("oracle_incdir", "${oracle_home}/include")
    macro("oracle_libdir", "${oracle_home}/lib")

    ctx.hwaf_declare_macro("oracle_export_paths", (
      {"default": ["${oracle_incdir}", "${oracle_libdir}", "${oracle_bindir}"]},
      {"target-win": ["${oracle_incdir}", "${oracle_bindir}"]},
    ))

    macro("LIB_oracle", (
      {"default": "clntsh"},
      {"target-win": "oci"},
    ))
    
    macro("TNS_ADMIN", "${oracle_home}/admin")
    ctx.hwaf_declare_runtime_env("TNS_ADMIN")
    
    ctx.hwaf_macro_append("oracle_export_paths", (
      {"default": "${TNS_ADMIN}"},
      {"ATLAS": ""},
    ))

    macro("ORA_FPU_PRECISION", "EXTEND")
    macro("NLS_LANG",          "AMERICAN_AMERICA.WE8ISO8859P1")

    ctx.hwaf_declare_runtime_env("ORA_FPU_PRECISION")
    ctx.hwaf_declare_runtime_env("NLS_LANG")
    
    ctx.lcg_declare_external_package(
        'oracle',
        path='${oracle_home}',
        binpath='${oracle_bindir}',
        incpath='${oracle_incdir}',
        libpath='${oracle_libdir}',
        )
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{set_ext_bin_and_lib_path [windir=bin unixdir=lib]})
    
    
    return # build

## EOF ##
