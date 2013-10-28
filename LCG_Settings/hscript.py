# -*- python -*-

## stdlib imports
import os
import os.path as osp
import sys

## waf imports
import waflib.Logs as msg
import waflib.Utils
import waflib.Configure
import waflib.Build
import waflib.Task
import waflib.Tools.ccroot
from waflib.Configure import conf
from waflib.TaskGen import feature, before_method, after_method, extension, after

PACKAGE = {
    'name': 'LCG_Settings',
    'author': ['atlas collaboration'],
}

def pkg_deps(ctx):
    return

### ---------------------------------------------------------------------------
def configure(ctx):
    
    msg.debug ('[configure] package name: '+PACKAGE['name'])

    macro = ctx.hwaf_declare_macro
    
    ### export
    ctx.hwaf_export_module("waftools/lcg-policy.py")

    macro("SITEROOT", (
        {"default": "/opt"},
        {("afs", "cern"): "/afs/cern.ch"},
        {("cvmfs", "cern"): "/cvmfs/cern.ch"},
    ))
    ctx.hwaf_declare_runtime_env("SITEROOT")
    
    macro("LCG_releases", (
      {"default": "${LCG_Settings_root}/../../.."},
      {("ATLAS", "NIGHTLIES"): "/afs/cern.ch/sw/lcg/app/nightlies/${LCG_NGT_SLT_NAME}/${LCG_NGT_DAY_NAME}"},
      {"ATLAS": "${SITEROOT}/sw/lcg/app/releases"},
    ))

    macro("LCG_external", (
      {"default": "${LCG_Settings_root}/../../../../../external"},
      {"ATLAS": "${SITEROOT}/sw/lcg/external"},
    ))

    macro("unixdirname", (
      {"default": "lib"},
      {("target-unix", "target-x86_64"): "lib64"},
    ))

    # ==== Compiler Names and environment setup ====

    # gcc
    macro("gcc_config_version", (
      {"default": ""},
      {"target-gcc43": "4.3.5"},
      {"target-gcc44": "4.4.3"},
      {"target-gcc45": "4.5.3"},
      {"target-gcc46": "4.6.2"},
      {"target-gcc47": "4.7.2"},
      {"target-gcc48": "4.8.1"},
      {"target-gccmax": "max"},
      {"target-g11max": "g11"},
      {"target-icc11": "4.3.5"},
      {"target-clang": "4.6.2"},
    ))

    macro("gcc_native_version", (
      {"default": "${gcc_config_version}"},
    ))

    macro("gcc_home", (
      {"default": "${LCG_external}/gcc/${gcc_native_version}/${LCG_hostos}"},
    ))

    # clang
    macro("clang_config_version", (
      {"default": ""},
      {"target-clang30": "3.0"},
      {"target-clang31": "3.1"},
    ))

    macro("clang_native_version", (
      {"default": "${clang_config_version}"},
    ))

    macro("clang_home", (
      {"default": "${LCG_external}/llvm/${clang_native_version}/${LCG_hostos}"},
    ))

    # icc
    macro("icc_config_version", (
      {"default": ""},
      {"target-icc11": "11.1"},
    ))

    macro("icc_native_version", (
      {"default": "${icc_config_version}"},
    ))

    macro("intelplat", (
      {"default": ""},
      {("target-icc", "target-i686"): "ia32"},
      {("target-icc", "target-x86_64"): "intel64"},
    ))
    ctx.hwaf_declare_runtime_env("intelplat")

    macro("intel_home", (
      {"default": ""},
      {"target-icc": "/afs/cern.ch/sw/IntelSoftware/linux"},
    ))
    ctx.hwaf_declare_runtime_env("intel_home")
    
    macro("icc_home", (
      {"default": ""},
      {"target-icc": "${intel_home}/x86_64/Compiler/${icc_native_version}"},
    ))
    ctx.hwaf_declare_runtime_env("icc_home")
    
    macro("icc_c_home", (
      {"default": ""},
      {"target-icc": "${icc_home}/072"},
    ))
    ctx.hwaf_declare_runtime_env("icc_c_home")
    
    macro("icc_f_home", (
      {"default": ""},
      {"target-icc": "${icc_home}/072"},
    ))
    ctx.hwaf_declare_runtime_env("icc_f_home")

    # LINKER
    ctx.hwaf_macro_append("LDFLAGS", (
      {"default":""},
      {("host-x86_64", "target-i686"): "-m32"}
    ))
    ctx.hwaf_declare_runtime_env("LDFLAGS")

    # C Preprocessor
    ctx.hwaf_macro_append("CPPFLAGS", (
      {"default":""},
      {("host-x86_64", "target-i686"): "-m32"}
    ))
    ctx.hwaf_declare_runtime_env("CPPFLAGS")
    
    # C Settings
    
    macro("CC", (
      {"default": "gcc"},
      {("CERNDISTCC", "target-slc", "target-gcc"): "lcg-gcc-${gcc_config_version}"},
      {("host-slc5", "target-gcc34"): "gcc34"},
      {"target-darwin": "cc"},
      {"target-win": "cl"},
      {"target-clang": "clang"},
      {"target-icc": "icc"},
    ), override=True,
    )
    ctx.hwaf_declare_runtime_env("CC")

    ctx.hwaf_macro_append("CFLAGS", (
      {"default":""},
      {("host-x86_64", "target-i686"): "-m32"}
    ))
    ctx.hwaf_declare_runtime_env("CFLAGS")

    ctx.hwaf_macro_append("CFLAGS", (
      {"default":""},
      {("target-c11"): "-std=c1x"}
    ))
    #ctx.hwaf_declare_runtime_env("CFLAGS")

    # C++ Settings
    
    macro("CXX", (
      {"default": "g++"},
      {("CERNDISTCC", "target-slc", "target-gcc"): "lcg-g++-${gcc_config_version}"},
      {("host-slc5", "target-gcc34"): "g++34"},
      {"target-darwin": "c++"},
      {"target-win": "cl"},
      {"target-clang": "clang++"},
      {"target-icc": "icpc"},
    ), override=True,
    )
    
    ctx.hwaf_declare_runtime_env("CXX")

    ctx.hwaf_macro_append("CXXFLAGS", (
      {"default":""},
      {("host-x86_64", "target-i686"): "-m32"}
    ))
    ctx.hwaf_declare_runtime_env("CXXFLAGS")

    ctx.hwaf_macro_append("CXXFLAGS", (
      {"default":""},
      {"target-c11": "-std=c++0x"},
    ))

    macro("LINK_CXX", (
      {"default": "${CXX}"},
      {"target-win": "link.exe"},
    ), override=True,
    )

    # Fortran settings
    macro("FC", (
      {"default": "g77"},
      {("CERNDISTCC", "target-slc", "target-gcc"): "lcg-gfortran-${gcc_config_version}"},
      {"target-gcc4": "gfortran"},
      {"target-win": "f77.exe"},
      {"target-clang": "gfortran"},
      {"target-icc": "ifort"},
    ), override=True,
    )
    ctx.hwaf_declare_runtime_env("FC")

    ctx.hwaf_macro_append("FCFLAGS", (
      {"default":""},
      {("host-x86_64", "target-i686"): "-m32"}
    ))
    ctx.hwaf_declare_runtime_env("FCFLAGS")

    # Distcc Settings
    ctx.hwaf_declare_tag(
        "CERNDISTCC",
        content=["CERN", "use-distcc"]
    )

    ctx.hwaf_macro_prepend("CPP", (
      {"default": ""},
      {"use-distcc": "distcc"},
    ))

    ctx.hwaf_macro_prepend("CC", (
      {"default": ""},
      {"use-distcc": "distcc"},
    ))

    ctx.hwaf_macro_prepend("FC", (
      {"default": ""},
      {"use-distcc": "distcc"},
    ))

    # Ccache Settings
    macro("CCACHE_PREFIX", (
      {"default": ""},
      {("use-ccache", "use-distcc"): "distcc"},
    ))
    ctx.hwaf_declare_runtime_env("CCACHE_PREFIX")

    ctx.hwaf_macro_remove("CPP", (
      {"default": ""},
      {("use-ccache", "use-distcc"): "distcc"},
    ))

    ctx.hwaf_macro_prepend("CPP", (
      {"default": ""},
      {"use-ccache": "ccache"},
    ))

    ctx.hwaf_macro_remove("CC", (
      {"default": ""},
      {("use-ccache", "use-distcc"): "distcc"},
    ))

    ctx.hwaf_macro_prepend("CC", (
      {"default": ""},
      {"use-ccache": "ccache"},
    ))

    ctx.hwaf_macro_remove("FC", (
      {"default": ""},
      {("use-ccache", "use-distcc"): "distcc"},
    ))

    ctx.hwaf_macro_prepend("FC", (
      {"default": ""},
      {"use-ccache": "ccache"},
    ))

    # Environment for special compilers
    ctx.hwaf_path_remove("PATH", (
      {"default": ""},
      {"target-lcg-compiler": "${LCG_external}/gcc/"},
      {"target-icc": "${LCG_external}/gcc/"},
      {"target-clang": "${LCG_external}/gcc/"},
    ))

    ctx.hwaf_path_remove("PATH", (
      {"default": ""},
      {"target-clang": "${LCG_external}/llvm/"},
    ))

    ctx.hwaf_path_prepend("PATH", (
      {"default": ""},
      {"target-lcg-compiler": "${gcc_home}/bin"},
      {"target-clang": "${gcc_home}/bin"},
      {"target-icc": "${gcc_home}/bin"},
    ))

    ctx.hwaf_path_prepend("PATH", (
      {"default": ""},
      {"target-clang": "${clang_home}/bin"},
    ))

    macro("LCG_COMPILER_ROOT", (
        {"default": ""},
        {"target-lcg-compiler": "${gcc_home}"},
        {"target-clang":        "${clang_home}"},
        {"target-icc":          "${icc_home}"},
        ))
    
    macro("COMPILER_PATH", (
      {"default": "${gcc_home}/lib/gcc/x86_64-unknown-linux-gnu/${gcc_native_version}"},
    ))
    ctx.hwaf_declare_runtime_env("COMPILER_PATH")

    ctx.hwaf_path_remove("LD_LIBRARY_PATH", (
      {"default": ""},
      {"target-lcg-compiler": "${LCG_external}/gcc/"},
      {"target-icc": "${LCG_external}/gcc/"},
      {"target-clang": "${LCG_external}/gcc/"},
    ))

    ctx.hwaf_path_remove("LD_LIBRARY_PATH", (
      {"default": ""},
      {"target-clang": "${LCG_external}/llvm/"},
    ))

    ctx.hwaf_path_prepend("LD_LIBRARY_PATH", (
      {"default": ""},
      {("target-lcg-compiler", "host-x86_64", "target-i686"): "${gcc_home}/lib64"},
      {("target-icc", "host-x86_64", "target-i686"): "${gcc_home}/lib64"},
      {"target-clang": "${clang_home}/lib"},
    ))

    ctx.hwaf_path_prepend("LD_LIBRARY_PATH", (
      {"default": ""},
      {"target-lcg-compiler": "${gcc_home}/${unixdirname}"},
      {"target-clang": "${gcc_home}/${unixdirname}"},
      {"target-icc": "${gcc_home}/${unixdirname}"},
    ))

    #code coverage - lcov tool
    macro("use_lcov", (
      {"default": ""},
      {"target-cov": ["lcov", "v*", "LCG_Interfaces"]},
    ))

    #profiling - igprof tool
    macro("use_igprof", (
      {"default": ""},
      {"target-pro": ["igprof", "v*", "LCG_Interfaces"]},
    ))

    #temporal ATLAS hack
    ctx.hwaf_macro_append("CFLAGS", (
      {"default": ""},
      {("ATLAS", "target-slc", "target-gcc45"): ["-include", "stdint.h"]},
      {("ATLAS", "target-slc", "target-gcc46"): ["-include", "stddef.h", "-include", "stdint.h"]},
    ))
    ctx.hwaf_macro_append("CXXFLAGS", (
      {"default": ""},
      {("ATLAS", "target-slc", "target-gcc45"): ["-include", "cstdio", "-include", "stdint.h"]},
      {("ATLAS", "target-slc", "target-gcc46"): ["-include", "stddef.h", "-include", "cstdio", "-include", "stdint.h"]},
    ))

    ### load-up toolchain
    msg.debug("lcg: loading toolchain...")
    msg.debug("lcg: path=%s" % (ctx.env["LCG_COMPILER_ROOT"]))
    ctx.load('find_compiler')
    path = ctx.env['LCG_COMPILER_ROOT']
    ctx.find_toolchain(override=True, path=path, mandatory=True)
    ctx.msg("LCG C compiler", ctx.env['CC'])
    ctx.msg("LCG CXX compiler", ctx.env['CXX'])
    ctx.msg("LCG Fortran compiler", ctx.env['FC'])
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
