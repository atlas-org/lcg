# -*- python -*-
# automatically generated wscript

import os.path as osp

import waflib.Logs as msg

PACKAGE = {
    'name': 'LCG_Interfaces/Python',
    'author': ["ATLAS Collaboration"], 
}

def pkg_deps(ctx):
    ctx.use_pkg("LCG_Configuration")
    ctx.use_pkg("LCG_Settings")
    return

def options(ctx):
    ctx.load('find_python')
    
def configure(ctx):
    msg.debug('[configure] package name: '+PACKAGE['name'])

    if ctx.hwaf_enabled_tag("STANDALONE"):
        ctx.load('find_python')
        ctx.find_python()

        py_home = osp.dirname(ctx.hwaf_subst_vars("${LIBPATH_PYEMBED}"))
        ctx.lcg_declare_external_package(
            'python',
            path=py_home,
            libpath='${LIBPATH_PYEMBED}',
            libname='${LIB_PYEMBED}',
            incpath='${INCLUDES_PYEMBED}',
            )
        return
    
    macro = ctx.hwaf_declare_macro
    
    ctx.hwaf_declare_tag("target-mac", content=["python_framework"])
    
    macro("Python_native_version", (
        {"default": "${Python_config_version}"},
        ))

    macro("Python_version", (
        {"default": "${Python_config_version_twodigit}"},
        ))
    
    macro("Python_libversion", (
        {"default": "${Python_config_version_twodigit}"},
        ## FIXME:
        #{"target-win": "${Python_libversion_cmd}"},
        ))
    
    macro("Python_home", (
        {"default": "${LCG_external}/Python/${Python_native_version}/${LCG_system}"},
        {"python_framework": "${LCG_external}/Python/${Python_native_version}/${LCG_system}/Python.framework/Versions/Current"},
        ))

    macro("Python_inc", (
        {"default": "${Python_home}/include/python${Python_version}"},
        {"target-win": "${Python_home}/include"}
        ))

    macro("Python_bindir", (
        {"default": "${Python_home}/bin"},
        {"target-win": "${Python_home}"}
        ))

    macro('Python_linkopts', (
        {'default': 'python${Python_libversion} util pthread'},
        {'target-darwin': 'python'},
        {'target-win': 'python${Python_libversion}'}
        ))

    if ctx.is_darwin():
        macro("PYTHONHOME", (
            {"default": ""},
            {"target-darwin": "${Python_home}"},
            ))
        ctx.hwaf_declare_runtime_env("PYTHONHOME")

    ctx.hwaf_path_prepend("LD_LIBRARY_PATH", (
        {"default": "${Python_home}/lib"},
        {"target-darwin": ""},
        {"target-win": ""},
        {"NO_PYTHON_LIBPATH":""},
        ))
    
    ctx.hwaf_path_prepend("DYLD_LIBRARY_PATH", (
        {"default": ""},
        {"target-darwin": "${Python_home}:${Python_home}/lib"},
        ))

    ctx.hwaf_path_prepend("PATH", (
        {"default": "${Python_bindir}"},
        ))
    
    ctx.load('find_python')
    if ctx.env['HWAF_FOUND_PYTHON']: del ctx.env['HWAF_FOUND_PYTHON']

    pyvers = tuple(map(int, ctx.hwaf_subst_vars("${Python_config_version_twodigit}").split(".")))
    path = ctx.hwaf_subst_vars("${Python_home}")
    binpath = ctx.hwaf_subst_vars("${Python_bindir}")

    ctx.find_python(
        version=pyvers,
        path_list=[binpath],
        extra_paths=[path],
        )
    
    ctx.lcg_declare_external_package(
        'python',
        path='${Python_home}',
        libpath='${Python_home}/lib',
        libname='${Python_linkopts}',
        incpath='${Python_inc}',
        )
    
    return

def build(ctx):
    return
