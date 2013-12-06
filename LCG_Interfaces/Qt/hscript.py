## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Interfaces/Qt",
    'author': ["ATLAS Collaboration"], 
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
    
    macro("Qt_native_version", "${qt_config_version}")
    macro("Qt_home", "${LCG_external}/qt/${Qt_native_version}/${LCG_system}")

    macro("Qt_export_paths", "${Qt_home}")
    macro("Qt_bindir", "${Qt_home}/bin")
    macro("Qt_incdir", "${Qt_home}/include")
    macro("Qt_libdir", "${Qt_home}/lib")
    
    macro("DEFINES_Qt", "QT_THREAD_SUPPORT")

    macro("LIB_Qt", (
      {"default": ["QtCore", "QtGui"]},
    ))

    macro("Qt_name", "qt")

    macro("QTDIR", "${Qt_home}", override=True)
    ctx.hwaf_declare_runtime_env("QTDIR")

    ctx.lcg_declare_external_package(
        "Qt",
        path="${Qt_home}",
        incpath="${Qt_incdir}",
        libpath="${Qt_libdir}",
        binpath="${Qt_bindir}",
        )

    libpath = ctx.hwaf_subst_vars("${Qt_libdir}")
    binpath = ctx.hwaf_subst_vars("${Qt_bindir}")
    incpath = ctx.hwaf_subst_vars("${Qt_incdir}")

    setattr(ctx.options,'qtdir', ctx.hwaf_subst_vars("${Qt_home}"))
    setattr(ctx.options,'qtbin', binpath)
    ctx.load("qt4")

    QT4_LIBS="QtCore QtGui QtUiTools QtNetwork QtOpenGL QtSql QtSvg QtTest QtXml QtXmlPatterns QtWebKit Qt3Support QtHelp QtScript QtDeclarative QtDesigner"
    for qtlib in QT4_LIBS.split():
        msg.debug('lcg: defining use-lib [%s]...' % (qtlib,))
        ctx.hwaf_define_uselib(
            qtlib,
            libpath=libpath,
            libname=qtlib,
            incpath=incpath,
            incname=None,
            )

    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
