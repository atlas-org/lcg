# -*- python -*-

## stdlib imports
import os
import os.path as osp
import sys

## waf imports
import waflib.Errors
import waflib.Logs as msg
import waflib.Utils
import waflib.Configure
import waflib.Build
import waflib.Task
import waflib.Tools.ccroot
from waflib.Configure import conf
from waflib.TaskGen import feature, before_method, after_method, extension, after


### ---------------------------------------------------------------------------
@conf
def lcg_declare_external_package(ctx, name, path,
                                 libpath=None, libname=None,
                                 incpath=None,
                                 binpath=None,
                                 pypath=None,
                                 manpath=None):
    """
    lcg_declare_external_package creates the proper uselib variables based on the ``name``
    """
    msg.debug ('lcg: declaring package [%s]...' % (name,))
    topdir = ctx.hwaf_subst_vars(path)
    path = ctx.root.find_dir(topdir)
    if not path:
        ctx.fatal('lcg: package [%s]: no such top directory [%s]' % (ctx.hwaf_pkg_name(), topdir,))
        pass
    
    # if libpath is None:
    #     libpath = osp.join(path, 'lib')
    # if incpath is None:
    #     incpath = osp.join(path, 'include')

    if libpath: libpath = ctx.hwaf_subst_vars(libpath)
    if libname: libname = ctx.hwaf_subst_vars(libname)
    if incpath: incpath = ctx.hwaf_subst_vars(incpath)
    if binpath: binpath = ctx.hwaf_subst_vars(binpath)
    if pypath:  pypath =  ctx.hwaf_subst_vars(pypath)
    if manpath: manpath = ctx.hwaf_subst_vars(manpath)

    if binpath and not binpath in ctx.env['PATH']:
        ctx.hwaf_path_prepend('PATH', binpath)
        pass

    if libpath and not libpath in ctx.env['LD_LIBRARY_PATH']:
        ctx.hwaf_path_prepend('LD_LIBRARY_PATH', libpath)
        pass
    
    if pypath and not pypath in ctx.env['PYTHONPATH']:
        ctx.hwaf_path_prepend('PYTHONPATH', pypath)
        pass

    if manpath and not manpath in ctx.env['MANPATH']:
        ctx.hwaf_path_prepend('MANPATH', manpath)
        pass

    return ctx.hwaf_define_uselib(name, libpath, libname, incpath, incname=None)

### ---------------------------------------------------------------------------
@conf
def lcg_install_external_package(ctx,
                                 name, path,
                                 libpath=None,
                                 incpath=None, incname=None,
                                 binpath=None,
                                 manpath=None,
                                 ):
    """
    lcg_install_external_package installs the external package under the ${INSTALL_AREA}
    """
    msg.debug ('lcg: installing external package [%s]...' % (name,))
    if incname is None:
        incname = name

    path = ctx.hwaf_subst_vars(path)
    root = ctx.root.find_dir(path)
    if not root:
        err = "lcg: external package [%s] has not such directory [%s]" % (name, root)
        msg.error(err)
        raise waflib.Errors.WafError(err)

    if incpath:
        incpath = ctx.hwaf_subst_vars(incpath)
        incdir = ctx.root.find_dir(incpath)
        if not incdir:
            err = "lcg: external package [%s] has not such directory [%s]" % (name, incpath)
            msg.error(err)
            raise waflib.Errors.WafError(err)
        ctx.install_files(
            '${INSTALL_AREA}/include/%s' % incname,
            incdir.ant_glob('**'),
            cwd = incdir.abspath(),
            relative_trick = True,
            postpone = False,
            )
        pass

    if libpath:
        libpath = ctx.hwaf_subst_vars(libpath)
        libdir = ctx.root.find_dir(libpath)
        if not libdir:
            err = "lcg: external package [%s] has not such directory [%s]" % (name, libpath)
            msg.error(err)
            raise waflib.Errors.WafError(err)
        ctx.install_files(
            '${INSTALL_AREA}/lib',
            libdir.ant_glob('**'),
            cwd = libdir.abspath(),
            relative_trick = True,
            postpone = False,
            )
        pass
    
    if binpath:
        binpath = ctx.hwaf_subst_vars(binpath)
        bindir = ctx.root.find_dir(binpath)
        if not bindir:
            err = "lcg: external package [%s] has not such directory [%s]" % (name, binpath)
            msg.error(err)
            raise waflib.Errors.WafError(err)
        ctx.install_files(
            '${INSTALL_AREA}/bin',
            bindir.ant_glob('**'),
            cwd = bindir.abspath(),
            relative_trick = True,
            postpone = False,
            )
        pass
    
    if manpath:
        manpath = ctx.hwaf_subst_vars(manpath)
        mandir = ctx.root.find_dir(manpath)
        if not mandir:
            err = "lcg: external package [%s] has not such directory [%s]" % (name, manpath)
            msg.error(err)
            raise waflib.Errors.WafError(err)
        ctx.install_files(
            '${INSTALL_AREA}/share/%s' % name,
            mandir.ant_glob('**'),
            cwd = bindir.abspath(),
            relative_trick = True,
            postpone = False,
            )
        pass
    
    return


## EOF ##
