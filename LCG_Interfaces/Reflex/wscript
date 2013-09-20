## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/Reflex",
    "authors": ["ATLAS Collaboration"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Configuration", version="v*", public=True)
    ctx.use_pkg("LCG_Settings", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/ROOT", version="v*", public=True)
    
    ## no private dependencies
    ## runtime dependencies
    ctx.use_pkg("LCG_Interfaces/ROOT", version="v*", runtime=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    macro = ctx.hwaf_declare_macro
    macro_append = ctx.hwaf_macro_append
    
    macro("Reflex_linkopts", "${ROOT_Reflex_linkopts}")
    macro("genreflex_cmd", (
      {"default": "${ROOT_home}/bin/genreflex"},
      {"target-win": "${ROOT_home}/bin/genreflex.bat"},
    ))

    macro("gccxmloptsval", (
      {"default": ["--gccxml-compiler", "${CXX_NAME}"]},
      {"target-clang": ["--gccxml-compiler", "gcc"]},
    ))

    macro_append("gccxmloptsval", (
      {"default": ""},
      {("host-x86_64", "target-i686"): ["--gccxml-cxxflags", "-m32"]},
      {("host-darwin", "target-i386"): ["--gccxml-cxxflags", "-m32"]},
      {("host-i686", "target-x86_64"): ["--gccxml-cxxflags", "-m64"]},
      {("host-darwin", "target-x86_64"): ["--gccxml-cxxflags", "-m64"]},
      {"target-gccmax": ["--gccxml-cxxflags", "-D__STRICT_ANSI__"]},
    ))

    macro("gccxmlopts", (
      {"default": "--gccxmlopt='${gccxmloptsval}'"},
      {"target-win": "--gccxmlopt=\"${gccxmloptsval}\""},
    ))

    macro("gccxml_cppflags", (
      {"default": ""},
      {"target-win": ["-DNDEBUG", "${cppmacros}"]},
    ))

    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
