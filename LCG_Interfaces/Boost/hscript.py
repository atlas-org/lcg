# -*- python -*-
# automatically generated wscript

import waflib.Logs as msg

PACKAGE = {
    'name': 'LCG_Interfaces/Boost',
    'author': ["ATLAS Collaboration"], 
}

def pkg_deps(ctx):
    ctx.use_pkg("LCG_Configuration")
    ctx.use_pkg("LCG_Settings")
    ctx.use_pkg("LCG_Interfaces/Python")
    return

### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options

def configure(ctx):
    msg.debug('[configure] package name: '+PACKAGE['name'])

    macro = ctx.hwaf_declare_macro
    
    macro("Boost_native_version", "${Boost_config_version}_python${Python_config_version_twodigit}")
    macro("Boost_home", "${LCG_external}/Boost/${Boost_native_version}/${LCG_system}")

    macro("Boost_compiler_version", (
      {"default": "${LCG_compiler}"},
      {"target-icc": "${gcc2icc}"},
      {"target-clang": "${gcc2clang}"},
      {"target-gccmax": "${gcc2max}"},
      {"target-g11max": "${gcc2g11}"},
      {("target-gcc42", "target-darwin"): "xgcc42"},
      {("target-gcc40", "target-darwin"): "xgcc40"},
      {"target-vc9": "vc90"},
    ))

    macro("Boost_incdir", "${Boost_home}/include/boost-${Boost_file_version}")
    macro("Boost_libdir", "${Boost_home}/lib")

    ctx.hwaf_macro_append("CPPFLAGS_boost", (
      {"default": ""},
      {"target-win": ["/DBOOST_ALL_DYN_LINK", "/wd4275", "/wd4251"]},
    ))
    
    ctx.hwaf_macro_append("DEFINES_boost", (
      {"default": ""},
      {"USE_BOOST_TIME_WITH_NSEC_RESOLUTION": "BOOST_DATE_TIME_POSIX_TIME_STD_CONFIG"},
    ))
    
    ctx.hwaf_macro_append("LIB_boost", (
      {"default": ""},
      {"USE_BOOST_TIME_WITH_NSEC_RESOLUTION": "${Boost_linkopts_date_time}"},
    ))

    ctx.hwaf_path_prepend('LD_LIBRARY_PATH', '${Boost_libdir}')
    
    incdir = ctx.hwaf_subst_vars("${Boost_incdir}")
    libdir = ctx.hwaf_subst_vars("${Boost_libdir}")
    
    ctx.lcg_declare_external_package(
        "boost",
        path="${Boost_home}",
        incpath=incdir,
        libpath=libdir,
    )

    ## define a minimal Boost-uselib
    macro("INCLUDES_Boost", "${Boost_incdir}")
    macro( "LIBPATH_Boost", "${Boost_libdir}")
    ##
    
    ctx.load('find_boost')
    path = ctx.hwaf_subst_vars("${Boost_home}")
    ctx.find_boost(
        path_list=[path],
        extra_paths=[path],
        includes=incdir,
        libs=libdir,
        )
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
