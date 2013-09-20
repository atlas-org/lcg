## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/uuid",
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
    
    macro("uuid_native_version", "${uuid_config_version}")
    macro("uuid_home", (
      {"default": "${LCG_external}/uuid/${uuid_native_version}/${LCG_system}"},
      {"target-slc6": "/usr"},
    ))
    
    ctx.hwaf_declare_macro("uuid_includes", (
      {"default": "${uuid_home}/include"},
      {"target-slc6": "."}, # hack to avoid "-I' '" on compilation time, -I. is harmless
    ))

    macro("uuid_incdir", "${uuid_includes}")
    macro("uuid_libdir", "${uuid_home}/lib")
    macro("uuid_mandir", "${uuid_home}/share/man")
    macro("uuid_bindir", "${uuid_home}/bin")

    macro("LIB_uuid", "uuid")
    
    macro("uuid_export_paths", (
      {"default": ["${uuid_incdir}", "${uuid_libdir}"]},
      {"target-slc6": ""},
    ))

    if not ctx.hwaf_enabled_tag('target-slc6'):
        ctx.lcg_declare_external_package(
            'uuid',
            path='${uuid_home}',
            binpath='${uuid_bindir}',
            incpath='${uuid_incdir}',
            libpath='${uuid_libdir}',
            manpath='${uuid_mandir}',
            )
        uuid_kwargs['extra_paths'] = [path]
        uuid_kwargs['path_list'] = [binpath]
        pass
        
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
