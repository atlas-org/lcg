## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/gdb",
    "authors": ["ATLAS Collaboration"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Configuration", version="v*", public=True)
    ctx.use_pkg("LCG_Settings", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/lcgdmcommon", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/epel", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/Python", version="v*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    macro = ctx.hwaf_declare_macro
    
    macro("gdb_native_version", "${gdb_config_version}")
    macro("gdb_home", "${LCG_external}/gdb/${gdb_native_version}/${LCG_system}")

    macro("gdb_bindir", "${gdb_home}/bin")
    macro("gdb_incdir", "${gdb_home}/include")
    macro("gdb_libdir", "${gdb_home}/lib")
    macro("gdb_mandir", "${gdb_home}/share/man")

    macro("STLIB_bfd", "bfd")
    ctx.hwaf_macro_prepend("STLIBPATH_bfd", (
        {"target-x86_64": ["${gdb_libdir}", "${gdb_home}/lib64"]},
        {"target-i686":   ["${gdb_libdir}"]},
    ))

    
    macro("gdb_export_paths", (
      {"default": ["${gdb_incdir}",
                   "${gdb_bindir}",
                   "${gdb_libdir}",
                   "${gdb_mandir}",
                   ]},
      {"target-x86_64": ["${gdb_incdir}",
                         "${gdb_bindir}",
                         "${gdb_libdir}",
                         "${gdb_home}/lib64",
                         "${gdb_mandir}",
                         ]},
    ))

    ctx.lcg_declare_external_package(
        'gdb',
        path='${gdb_home}',
        binpath='${gdb_bindir}',
        incpath='${gdb_incdir}',
        libpath='${gdb_libdir}',
        #pypath='${gdb_pydir}',
        manpath='${gdb_mandir}',
        )

    path = ctx.hwaf_subst_vars('${gdb_home}')
    binpath = ctx.hwaf_subst_vars('${gdb_bindir}')
    ctx.load('find_gdb')
    ctx.find_gdb(
        path_list=[binpath],
        extra_paths=[path],
        )
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    return # build

## EOF ##
