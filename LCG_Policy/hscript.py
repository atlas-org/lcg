## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Policy",
    "authors": ["ATLAS Collaboration"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Settings", version="", public=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    macro = ctx.hwaf_declare_macro
    
    macro("application_suffix", (
      {"default": ""},
      {"target-winxp": ".exe"},
    ))

    macro("cmt_installarea_prefix", "..")

    macro("cmt_installarea_command", (
      {"default": "cp"},
      {"target-winxp": "copy"},
    ))

    macro("gcov_linkopts", (
      {"default": ""},
      {"target-cov": "${COMPILER_PATH}/libgcov.a"},
    ))

    macro("icc_linkopts", (
      {"default": ""},
      {"target-icc": ["-L${gcc_home}/${unixdirname}", "-lstdc++"]},
      {"target-clang": ["-L${gcc_home}/${unixdirname}", "-lstdc++"]},
    ))
    ##### **** statement *hlib.PatternStmt (&{include_dir_policy -global include_path none ; include_dirs $(<PACKAGE>ROOT)})
    ##### **** statement *hlib.PatternStmt (&{install_includes -global document install_includes install_includes})
    ##### **** statement *hlib.PatternStmt (&{install_pythonmods -global macro run_install_pythonmods do_install_pythonmods ATLAS dont_install_pythonmods ; apply_pattern $(run_install_pythonmods)})
    ##### **** statement *hlib.PatternStmt (&{do_install_pythonmods document install_pythonmods install_pythonmods})
    ##### **** statement *hlib.PatternStmt (&{dont_install_pythonmods })
    ##### **** statement *hlib.PatternStmt (&{lcg_shared_library_settings macro <package>_linkopts -llcg_<package> target-winxp lcg_<package>.lib ; private ; macro lcg_<package>_shlibflags $(libraryshr_linkopts) $(cmt_installarea_linkopts) $(lcg_<package>_use_linkopts) ; macro_remove lcg_<package>_use_linkopts $(<package>_linkopts) ; end_private})
    ##### **** statement *hlib.PatternStmt (&{lcg_shared_library library lcg_<package> -no_prototypes *.cpp ; apply_pattern lcg_shared_library_settings})
    ##### **** statement *hlib.PatternStmt (&{lcg_shared_generic_library library lcg_<package> -no_prototypes <files> ; apply_pattern lcg_shared_library_settings})
    ##### **** statement *hlib.PatternStmt (&{lcg_module_library library lcg_<package> *.cpp private ; macro lib_<package>_cppflags  target-winxp -DPLUGIN_MANAGER_SAMPLE_BUILD_DLL macro lcg_<package>_shlibflags $(libraryshr_linkopts) $(use_linkopts) target-darwin $(libraryshr_linkopts) $(use_linkopts) macro_remove use_linkopts $(<package>_linkopts) ; end_private})
    ##### **** statement *hlib.PatternStmt (&{lcg_module_generic_library library lcg_<name> <files> private ; macro lib_<name>_cppflags  target-winxp -DPLUGIN_MANAGER_SAMPLE_BUILD_DLL macro lcg_<name>_shlibflags $(libraryshr_linkopts) $(use_linkopts) macro_remove use_linkopts $(<package>_linkopts) ; end_private})
    ##### **** statement *hlib.PatternStmt (&{lcg_plugin_library library lcg_<package> *.cpp private ; macro lcg_<package>_shlibflags $(libraryshr_linkopts) $(use_linkopts) macro_remove use_linkopts $(<package>_linkopts) ; document genmap lcg_<package>RootMap LIBNAME=lcg_<package> ROOTMAP_DIR=$(CMTINSTALLAREA)/$(CMTCONFIG)/lib ; macro_append lcg_<package>RootMap_dependencies lcg_<package> ; end_private})
    ##### **** statement *hlib.PatternStmt (&{lcg_plugin_generic_library library lcg_<name> <files> private ; macro lcg_<name>_shlibflags $(libraryshr_linkopts) $(use_linkopts) macro_remove use_linkopts $(<name>_linkopts) ; document genmap lcg_<name>RootMap LIBNAME=lcg_<name> ROOTMAP_DIR=$(CMTINSTALLAREA)/$(CMTCONFIG)/lib ; macro_append lcg_<name>RootMap_dependencies lcg_<name> ; end_private})
    ##### **** statement *hlib.PatternStmt (&{library_path path_remove LD_LIBRARY_PATH /<package>/ target-winxp \<package>" ; path_append LD_LIBRARY_PATH target-winxp ${<PACKAGE>ROOT}/${BINDIR} ; apply_pattern library_Softlinks library="<library>})
    ##### **** statement *hlib.PatternStmt (&{package_library_os macro <package>_<name>_libs <unixlib> target-darwin <darwinlib> target-winxp <winlib> pattern <package>_use_<name> macro_append <package>_linkopts $(<package>_<name>_libs)})
    ##### **** statement *hlib.PatternStmt (&{package_library apply_pattern package_library_os name=<name> unixlib="-l<lib> darwinlib="-l<lib> winlib="<lib>.lib})
    ##### **** statement *hlib.PatternStmt (&{package_library_os_dep apply_pattern package_library_os name=<name> unixlib=<unixlib> darwinlib=<darwinlib> winlib=<winlib> apply_pattern <package>_use_<needed>})
    ##### **** statement *hlib.PatternStmt (&{package_library_dep apply_pattern package_library name=<name> lib=<lib> apply_pattern <package>_use_<needed>})
    #### macro &{{merge_rootmap_cmd [{default [${LCG_Policy_root}/cmt/fragments/merge_files.py]}]}}
    macro("merge_rootmap_cmd", (
      {"default": "${LCG_Policy_root}/cmt/fragments/merge_files.py"},
    ))
    ##### **** statement *hlib.PatternStmt (&{lcg_cond_mkdir action lcg_mkdir if [ ! -d <dir> ]; then mkdir -p <dir>; fi target-winxp if not exist <dir> mkdir <dir>"})
    ##### **** statement *hlib.PatternStmt (&{lcg_cond_mkdir_with_dep apply_pattern lcg_cond_mkdir dir=<dir> ; macro_append <tstexp>s_constituents lcg_mkdir ; macro <tstexp>_<name>_dependencies lcg_mkdir})
    ##### **** statement *hlib.PatternStmt (&{lcg_tstexp_application apply_pattern lcg_cond_mkdir_with_dep dir=$(CMTINSTALLAREA)/$(CMTCONFIG)/<tstexp>s/lib tstexp=<tstexp> name=<name> application <tstexp>_<name> -group=<tstexp>s -suffix=<name> -import=<import> -import=<import2> <files> bindirname="<tstexp>s/bin macro_append <tstexp>_<name>linkopts $(<package>_linkopts) -L$(CMTINSTALLAREA)/$(CMTCONFIG)/<tstexp>s/lib $(<package>_<tstexp>linkopts) $(gcov_linkopts) $(icc_linkopts) target-winxp $(<package>_linkopts) /LIBPATH:$(CMTINSTALLAREA)/$(CMTCONFIG)/<tstexp>s/lib $(<package>_<tstexp>linkopts)})
    ##### **** statement *hlib.PatternStmt (&{lcg_tstexp_library apply_pattern lcg_cond_mkdir_with_dep dir=$(CMTINSTALLAREA)/$(CMTCONFIG)/<tstexp>s/lib tstexp=<tstexp> name=<name> library <tstexp>_<name> -group=<tstexp>s -suffix=<name> <files> libdirname="<tstexp>s/lib macro <tstexp>_<name>_shlibflags $(libraryshr_linkopts) $(<package>_linkopts) -L$(CMTINSTALLAREA)/$(CMTCONFIG)/<tstexp>s/lib $(use_linkopts) $(gcov_linkopts) $(icc_linkopts) target-winxp $(libraryshr_linkopts) $(<package>_linkopts) /LIBPATH:$(CMTINSTALLAREA)/$(CMTCONFIG)/<tstexp>s/lib $(use_linkopts) macro_append <package>_<tstexp>linkopts -l<tstexp>_<name> target-winxp <tstexp>_<name>.lib})
    ##### **** statement *hlib.PatternStmt (&{lcg_tstexp_module apply_pattern lcg_cond_mkdir_with_dep dir=$(CMTINSTALLAREA)/$(CMTCONFIG)/<tstexp>s/lib tstexp=<tstexp> name=<name> library <tstexp>_<name> -group=<tstexp>s -suffix=<name> <files> libdirname="<tstexp>s/lib macro lib_<tstexp>_<name>_cppflags  target-winxp -DPLUGIN_MANAGER_SAMPLE_BUILD_DLL macro <tstexp>_<name>_shlibflags $(libraryshr_linkopts) $(<package>_linkopts) -L$(CMTINSTALLAREA)/$(CMTCONFIG)/<tstexp>s/lib $(<package>_<tstexp>linkopts) $(use_linkopts) target-winxp $(libraryshr_linkopts) $(<package>_linkopts) /LIBPATH:$(CMTINSTALLAREA)/$(CMTCONFIG)/<tstexp>s/lib $(<package>_<tstexp>linkopts) $(use_linkopts)})
    ##### **** statement *hlib.PatternStmt (&{lcg_test_application apply_pattern lcg_tstexp_application tstexp=test import=<import> import2=<import2> files=<files> name=<name>})
    ##### **** statement *hlib.PatternStmt (&{lcg_test_library apply_pattern lcg_tstexp_library tstexp=test files=<files> name=<name>})
    ##### **** statement *hlib.PatternStmt (&{lcg_test_module apply_pattern lcg_tstexp_module tstexp=test files=<files> name=<name>})
    ##### **** statement *hlib.PatternStmt (&{lcg_test_python action tests cp ../tests/test_*.py $(<package>_cmtpath)/../$(tag)/tests/bin/. chmod a+x $(<package>_cmtpath)/../$(tag)/tests/bin/test_*.py target-winxp copy ..\tests\test_*.py $(<package>_cmtpath)\..\$(tag)\tests\bin\*})
    ##### **** statement *hlib.PatternStmt (&{lcg_unit_test_application apply_pattern lcg_tstexp_application tstexp=test import=CppUnit import2=<import2> files=<files> name=<name>})
    ##### **** statement *hlib.PatternStmt (&{lcg_unit_test_library apply_pattern lcg_tstexp_library tstexp=test files=<files> name=<name>})
    ##### **** statement *hlib.PatternStmt (&{lcg_unit_test_module apply_pattern lcg_tstexp_module tstexp=test files=<files> name=<name>})
    ##### **** statement *hlib.PatternStmt (&{lcg_test_python action tests cp ../tests/test_*.py $(<package>_cmtpath)/../$(tag)/tests/bin/. chmod a+x $(<package>_cmtpath)/../$(tag)/tests/bin/test_*.py target-winxp copy ..\tests\test_*.py $(<package>_cmtpath)\..\$(tag)\tests\bin\*})
    ##### **** statement *hlib.PatternStmt (&{lcg_example_application apply_pattern lcg_tstexp_application tstexp=example files=<files> name=<name>})
    ##### **** statement *hlib.PatternStmt (&{lcg_example_library apply_pattern lcg_tstexp_library tstexp=example files=<files> name=<name>})
    ##### **** statement *hlib.PatternStmt (&{lcg_example_module apply_pattern lcg_tstexp_module tstexp=example files=<files> name=<name>})
    ##### **** statement *hlib.TagExcludeStmt (&{debug [optimized]})
    #### tag &{windebug [debug]}
    ctx.hwaf_declare_tag(
        "windebug",
        content=["debug"]
    )
    #### tag &{static [UnixStatic]}
    ctx.hwaf_declare_tag(
        "static",
        content=["UnixStatic"]
    )
    ##### **** statement *hlib.MakeFragmentStmt (&{vcproj_library_header})
    ##### **** statement *hlib.MakeFragmentStmt (&{vcproj_application_header})
    ##### **** statement *hlib.MakeFragmentStmt (&{vcproj_all})
    ##### **** statement *hlib.MakeFragmentStmt (&{vcproj_trailer})
    ##### **** statement *hlib.MakeFragmentStmt (&{vcproj_contents})
    ##### **** statement *hlib.MakeFragmentStmt (&{vcproj_directory_header})
    ##### **** statement *hlib.MakeFragmentStmt (&{vcproj_directory_trailer})
    ##### **** statement *hlib.MakeFragmentStmt (&{sln_header})
    ##### **** statement *hlib.MakeFragmentStmt (&{sln_project})
    ##### **** statement *hlib.MakeFragmentStmt (&{sln_trailer})
    ##### **** statement *hlib.MakeFragmentStmt (&{sln_project_config})
    ##### **** statement *hlib.MakeFragmentStmt (&{sln_dependency_project})
    ##### **** statement *hlib.MakeFragmentStmt (&{sln_dependency_header})
    ##### **** statement *hlib.MakeFragmentStmt (&{sln_dependency_trailer})
    ##### **** statement *hlib.MakeFragmentStmt (&{install_pythonmods})
    ##### **** statement *hlib.MakeFragmentStmt (&{application})
    ##### **** statement *hlib.MakeFragmentStmt (&{library})
    ##### **** statement *hlib.MakeFragmentStmt (&{install_includes_header})

    macro("vsCONFIG", (
      {"default": "Release"},
      {"debug": "Debug"},
    ))

    macro("vsDebug", (
      {"default": "2"},
      {"debug": "1"},
    ))

    macro("vsOptimize", (
      {"default": "2"},
      {"debug": "0"},
    ))
    #### macro &{{vsVersion [{default []} {target-vc71 [7.10]} {target-vc9 [9.00]}]}}
    macro("vsVersion", (
      {"default": ""},
      {"target-vc71": "7.10"},
      {"target-vc9": "9.00"},
    ))
    #### macro &{{package_GUID [{default [{8BC9CEB8-8B4A-11D0-8D11-00A0C91BC942}]}]}}
    macro("package_GUID", (
      {"default": "{8BC9CEB8-8B4A-11D0-8D11-00A0C91BC942}"},
    ))
    #### macro &{{GUID_all [{default [{8BC9CEB8-8B4A-11D0-8D11-00A0C91BC955}]}]}}
    macro("GUID_all", (
      {"default": "{8BC9CEB8-8B4A-11D0-8D11-00A0C91BC955}"},
    ))
    #### macro &{{cppdebugflags [{default []} {target-dbg [${cppdebugflags_s}]} {target-opt [${cppoptimized_s}]}]}}
    macro("cppdebugflags", (
      {"default": ""},
      {"target-dbg": "${cppdebugflags_s}"},
      {"target-opt": "${cppoptimized_s}"},
    ))
    #### macro &{{cppdebugflags_s [{default [-g]} {target-winxp [/Od /Z7]}]}}
    macro("cppdebugflags_s", (
      {"default": "-g"},
      {"target-winxp": ["/Od", "/Z7"]},
    ))
    #### macro &{{cppoptimized_s [{default [-O2]} {target-winxp []}]}}
    macro("cppoptimized_s", (
      {"default": "-O2"},
      {"target-winxp": ""},
    ))
    #### macro &{{cppprofiled_s [{default [-pg]} {target-winxp []}]}}
    macro("cppprofiled_s", (
      {"default": "-pg"},
      {"target-winxp": ""},
    ))
    #### macro_append &{{cppdebugflags [{default []} {target-prf [${cppprofiled_s}]}]}}
    ctx.hwaf_macro_append("cppdebugflags", (
      {"default": ""},
      {"target-prf": "${cppprofiled_s}"},
    ))
    #### macro &{{cdebugflags [{default []} {target-dbg [${cdebugflags_s}]}]}}
    macro("cdebugflags", (
      {"default": ""},
      {"target-dbg": "${cdebugflags_s}"},
    ))
    #### macro &{{cdebugflags_s [{default [-g target-winxp /Od /Z7 /D _DEBUG]}]}}
    macro("cdebugflags_s", (
      {"default": ["-g", "target-winxp", "/Od", "/Z7", "/D", "_DEBUG"]},
    ))
    #### macro &{{fdebugflags [{default []} {target-dbg [${fdebugflags_s}]}]}}
    macro("fdebugflags", (
      {"default": ""},
      {"target-dbg": "${fdebugflags_s}"},
    ))
    #### macro &{{fdebugflags_s [{default [-g target-winxp /nopdbfile]} {/debug:full [/optimize:0]}]}}
    macro("fdebugflags_s", (
      {"default": ["-g", "target-winxp", "/nopdbfile"]},
      {"/debug:full": "/optimize:0"},
    ))
    #### macro &{{foptimized_s [{default [-O2]} {target-winxp []}]}}
    macro("foptimized_s", (
      {"default": "-O2"},
      {"target-winxp": ""},
    ))
    #### macro_append &{{fdebugflags [{default []} {target-opt [${foptimized_s}]}]}}
    ctx.hwaf_macro_append("fdebugflags", (
      {"default": ""},
      {"target-opt": "${foptimized_s}"},
    ))
    #### macro &{{fprofiled_s [{default [-pg]} {target-winxp []}]}}
    macro("fprofiled_s", (
      {"default": "-pg"},
      {"target-winxp": ""},
    ))
    #### macro_append &{{fdebugflags [{default []} {target-prf [${fprofiled_s}]}]}}
    ctx.hwaf_macro_append("fdebugflags", (
      {"default": ""},
      {"target-prf": "${fprofiled_s}"},
    ))
    #### macro &{{linkdebugflags [{default []} {target-dbg [${linkdebugflags_s}]}]}}
    macro("linkdebugflags", (
      {"default": ""},
      {"target-dbg": "${linkdebugflags_s}"},
    ))
    #### macro &{{linkdebugflags_s [{default []} {target-winxp [/debug /verbose:lib]}]}}
    macro("linkdebugflags_s", (
      {"default": ""},
      {"target-winxp": ["/debug", "/verbose:lib"]},
    ))
    #### macro &{{cppmacros [{default [-Df2cFortran -fPIC -D_GNU_SOURCE -Dlinux -Dunix]} {target-darwin []} {target-winxp [-D"WIN32 -D"_MBCS -D"_WINDOWS]}]}}
    macro("cppmacros", (
      {"default": ["-Df2cFortran", "-fPIC", "-D_GNU_SOURCE", "-Dlinux", "-Dunix"]},
      {"target-darwin": ""},
      {"target-winxp": ["-D\"WIN32", "-D\"_MBCS", "-D\"_WINDOWS"]},
    ))
    #### macro &{{cppflags [{default [${cppmacros} -fPIC -pipe -ansi -Wall -W -pthread]} {target-mac105 [${cppmacros} -pipe -ansi -pedantic -W -Wall -Wno-non-virtual-dtor -Wno-long-long -Wno-long-double -Wwrite-strings -Wpointer-arith -Woverloaded-virtual -ftemplate-depth-512 -fmessage-length=0 -g]} {target-darwin [${cppmacros} -pipe -ansi -pedantic -W -Wall -Wno-non-virtual-dtor -Wno-long-long -Wwrite-strings -Wpointer-arith -Woverloaded-virtual -ftemplate-depth-512 -fmessage-length=0 -g]} {target-vc71 [${includes} ${cppmacros} /FD /c /nologo /W3 /GX /MD /GR /Zm500 /GF /GS]} {target-vc9 [${includes} ${cppmacros} /FD /c /nologo /W3 /EHsc /MD /GR /Zm500 /GF /GS]}]}}
    macro("cppflags", (
      {"default": ["${cppmacros}", "-fPIC", "-pipe", "-ansi", "-Wall", "-W", "-pthread"]},
      {"target-mac105": ["${cppmacros}", "-pipe", "-ansi", "-pedantic", "-W", "-Wall", "-Wno-non-virtual-dtor", "-Wno-long-long", "-Wno-long-double", "-Wwrite-strings", "-Wpointer-arith", "-Woverloaded-virtual", "-ftemplate-depth-512", "-fmessage-length=0", "-g"]},
      {"target-darwin": ["${cppmacros}", "-pipe", "-ansi", "-pedantic", "-W", "-Wall", "-Wno-non-virtual-dtor", "-Wno-long-long", "-Wwrite-strings", "-Wpointer-arith", "-Woverloaded-virtual", "-ftemplate-depth-512", "-fmessage-length=0", "-g"]},
      {"target-vc71": ["${includes}", "${cppmacros}", "/FD", "/c", "/nologo", "/W3", "/GX", "/MD", "/GR", "/Zm500", "/GF", "/GS"]},
      {"target-vc9": ["${includes}", "${cppmacros}", "/FD", "/c", "/nologo", "/W3", "/EHsc", "/MD", "/GR", "/Zm500", "/GF", "/GS"]},
    ))
    #### macro &{{gcov_cppflags [{default [-fprofile-arcs -ftest-coverage]}]}}
    macro("gcov_cppflags", (
      {"default": ["-fprofile-arcs", "-ftest-coverage"]},
    ))
    ##### **** statement *hlib.TagExcludeStmt (&{RELAX [target-c11]})
    #### macro_append &{{cppflags [{default []} {RELAX []} {target-c11 [-std=c++0x]}]}}
    ctx.hwaf_macro_append("cppflags", (
      {"default": ""},
      {"RELAX": ""},
      {"target-c11": "-std=c++0x"},
    ))
    #### macro_append &{{cppflags [{default []} {host-x86_64&target-i686&target-icc [-m32 -w1]} {target-icc [-w1]} {host-x86_64&target-i686 [-m32]} {host-darwin&target-i386 [-m32]} {host-i686&target-x86_64 [-m64]} {target-gcc&target-cov [${gcov_cppflags}]}]}}
    ctx.hwaf_macro_append("cppflags", (
      {"default": ""},
      {("host-x86_64", "target-i686", "target-icc"): ["-m32", "-w1"]},
      {"target-icc": "-w1"},
      {("host-x86_64", "target-i686"): "-m32"},
      {("host-darwin", "target-i386"): "-m32"},
      {("host-i686", "target-x86_64"): "-m64"},
      {("target-gcc", "target-cov"): "${gcov_cppflags}"},
    ))
    #### macro_remove &{{cppflags [{default []} {target-icc [-Wall -W]}]}}
    ctx.hwaf_macro_remove("cppflags", (
      {"default": ""},
      {"target-icc": ["-Wall", "-W"]},
    ))
    #### macro &{{ppcmd [{default [-I]}]}}
    macro("ppcmd", (
      {"default": "-I"},
    ))
    #### macro &{{cflags [{default [${cppflags}]}]}}
    macro("cflags", (
      {"default": "${cppflags}"},
    ))
    #### macro_append &{{cflags [{default []} {host-x86_64&target-i686 [-m32]} {host-darwin&target-i386 [-m32]} {host-i686&target-x86_64 [-m64]} {host-i386&target-x86_64 [-m64]}]}}
    ctx.hwaf_macro_append("cflags", (
      {"default": ""},
      {("host-x86_64", "target-i686"): "-m32"},
      {("host-darwin", "target-i386"): "-m32"},
      {("host-i686", "target-x86_64"): "-m64"},
      {("host-i386", "target-x86_64"): "-m64"},
    ))
    #### macro_append &{{cflags [{default []} {RELAX []} {target-c11 [-std=c1x]}]}}
    ctx.hwaf_macro_append("cflags", (
      {"default": ""},
      {"RELAX": ""},
      {"target-c11": "-std=c1x"},
    ))
    #### macro &{{fflags [{default [-O -fno-automatic -fdollar-ok -ff90 -w]} {target-winxp [/compile_only /nologo /warn:nofileopt /warn:nouncalled /fpp:"/m /fpp:"/I..]}]}}
    macro("fflags", (
      {"default": ["-O", "-fno-automatic", "-fdollar-ok", "-ff90", "-w"]},
      {"target-winxp": ["/compile_only", "/nologo", "/warn:nofileopt", "/warn:nouncalled", "/fpp:\"/m", "/fpp:\"/I.."]},
    ))
    #### macro_append &{{fflags [{default []} {host-x86_64&target-i686 [-m32]} {host-darwin&target-i386 [-m32]} {host-i686&target-x86_64 [-m64]} {host-i386&target-x86_64 [-m64]}]}}
    ctx.hwaf_macro_append("fflags", (
      {"default": ""},
      {("host-x86_64", "target-i686"): "-m32"},
      {("host-darwin", "target-i386"): "-m32"},
      {("host-i686", "target-x86_64"): "-m64"},
      {("host-i386", "target-x86_64"): "-m64"},
    ))
    #### macro &{{fcomp [{default [${for} -c ${fincludes} ${fdebugflags} ${fflags} ${pp_fflags}]} {target-winxp [${for} ${fdebugflags} ${fflags} ${pp_fflags}]}]}}
    macro("fcomp", (
      {"default": ["${for}", "-c", "${fincludes}", "${fdebugflags}", "${fflags}", "${pp_fflags}"]},
      {"target-winxp": ["${for}", "${fdebugflags}", "${fflags}", "${pp_fflags}"]},
    ))
    #### macro &{{makeLinkMap [{default [target-linux -Wl,-Map,Linux.map]} {target-winxp [/map]}]}}
    macro("makeLinkMap", (
      {"default": ["target-linux", "-Wl,-Map,Linux.map"]},
      {"target-winxp": "/map"},
    ))
    #### macro &{{cpplinkflags [{default []} {target-darwin [-bind_at_load]} {target-linux [-ldl -fpic -pthread -Wl,-E]} {target-winxp [/nologo /machine:ix86 ${linkdebugflags} ${makeLinkMap} /nodefaultlib kernel32.lib user32.lib ws2_32.lib advapi32.lib dbghelp.lib msvcprt.lib msvcrt.lib Netapi32.lib oldnames.lib]}]}}
    macro("cpplinkflags", (
      {"default": ""},
      {"target-darwin": "-bind_at_load"},
      {"target-linux": ["-ldl", "-fpic", "-pthread", "-Wl,-E"]},
      {"target-winxp": ["/nologo", "/machine:ix86", "${linkdebugflags}", "${makeLinkMap}", "/nodefaultlib", "kernel32.lib", "user32.lib", "ws2_32.lib", "advapi32.lib", "dbghelp.lib", "msvcprt.lib", "msvcrt.lib", "Netapi32.lib", "oldnames.lib"]},
    ))
    #### macro_append &{{cpplinkflags [{default [target-slc5&target-x86_64]} {-Wl,-z,max-page-size=0x1000 [UnixStatic]} {-ldl []}]}}
    ctx.hwaf_macro_append("cpplinkflags", (
      {"default": "target-slc5&target-x86_64"},
      {"-Wl,-z,max-page-size=0x1000": "UnixStatic"},
      {"-ldl": ""},
    ))
    #### macro_append &{{cpplinkflags [{default []} {target-prf [${cppprofiled_s}]}]}}
    ctx.hwaf_macro_append("cpplinkflags", (
      {"default": ""},
      {"target-prf": "${cppprofiled_s}"},
    ))
    #### macro_append &{{cpplinkflags [{default []} {host-x86_64&target-i686 [-m32]} {host-darwin&target-i386 [-m32]} {host-i686&target-x86_64 [-m64]} {host-i386&target-x86_64 [-m64]}]}}
    ctx.hwaf_macro_append("cpplinkflags", (
      {"default": ""},
      {("host-x86_64", "target-i686"): "-m32"},
      {("host-darwin", "target-i386"): "-m32"},
      {("host-i686", "target-x86_64"): "-m64"},
      {("host-i386", "target-x86_64"): "-m64"},
    ))
    #### macro &{{cpplink [{default [${cpplinkname} ${cpplinkflags}]}]}}
    macro("cpplink", (
      {"default": ["${cpplinkname}", "${cpplinkflags}"]},
    ))
    #### macro &{{componentshr_linkopts [{default []} {target-linux [-shared -fPIC -Wl,-s -ldl -pthread]} {target-winxp [/DLL /Export:getFactoryEntries]}]}}
    macro("componentshr_linkopts", (
      {"default": ""},
      {"target-linux": ["-shared", "-fPIC", "-Wl,-s", "-ldl", "-pthread"]},
      {"target-winxp": ["/DLL", "/Export:getFactoryEntries"]},
    ))
    #### macro_append &{{componentshr_linkopts [{default []} {target-slc5&target-x86_64 [-Wl,-z,max-page-size=0x1000]}]}}
    ctx.hwaf_macro_append("componentshr_linkopts", (
      {"default": ""},
      {("target-slc5", "target-x86_64"): ["-Wl,-z,max-page-size=0x1000"]},
    ))
    #### macro_append &{{componentshr_linkopts [{default []} {host-x86_64&target-i686 [-m32]} {host-darwin&target-i386 [-m32]} {host-i686&target-x86_64 [-m64]} {host-i386&target-x86_64 [-m64]}]}}
    ctx.hwaf_macro_append("componentshr_linkopts", (
      {"default": ""},
      {("host-x86_64", "target-i686"): "-m32"},
      {("host-darwin", "target-i386"): "-m32"},
      {("host-i686", "target-x86_64"): "-m64"},
      {("host-i386", "target-x86_64"): "-m64"},
    ))
    #### macro_remove &{{componentshr_linkopts [{default []} {target-dbg [-Wl,-s]}]}}
    ctx.hwaf_macro_remove("componentshr_linkopts", (
      {"default": ""},
      {"target-dbg": ["-Wl,-s"]},
    ))
    #### macro &{{libraryshr_linkopts [{default []} {target-linux [-shared -fPIC -ldl -pthread]} {target-winxp [/DLL]}]}}
    macro("libraryshr_linkopts", (
      {"default": ""},
      {"target-linux": ["-shared", "-fPIC", "-ldl", "-pthread"]},
      {"target-winxp": "/DLL"},
    ))
    #### macro_append &{{libraryshr_linkopts [{default []} {target-slc5&target-x86_64 [-Wl,-z,max-page-size=0x1000]}]}}
    ctx.hwaf_macro_append("libraryshr_linkopts", (
      {"default": ""},
      {("target-slc5", "target-x86_64"): ["-Wl,-z,max-page-size=0x1000"]},
    ))
    #### macro_append &{{libraryshr_linkopts [{default []} {target-cov [${gcov_linkopts}]} {target-icc [${icc_linkopts}]} {target-clang [${icc_linkopts}]}]}}
    ctx.hwaf_macro_append("libraryshr_linkopts", (
      {"default": ""},
      {"target-cov": "${gcov_linkopts}"},
      {"target-icc": "${icc_linkopts}"},
      {"target-clang": "${icc_linkopts}"},
    ))
    #### macro_append &{{libraryshr_linkopts [{default []} {host-x86_64&target-i686 [-m32]} {host-darwin&target-i386 [-m32]} {host-i686&target-x86_64 [-m64]} {host-i386&target-x86_64 [-m64]}]}}
    ctx.hwaf_macro_append("libraryshr_linkopts", (
      {"default": ""},
      {("host-x86_64", "target-i686"): "-m32"},
      {("host-darwin", "target-i386"): "-m32"},
      {("host-i686", "target-x86_64"): "-m64"},
      {("host-i386", "target-x86_64"): "-m64"},
    ))
    #### macro &{{application_linkopts [{default []} {target-linux [-Wl,--export-dynamic]}]}}
    macro("application_linkopts", (
      {"default": ""},
      {"target-linux": ["-Wl,--export-dynamic"]},
    ))
    #### macro &{{shlibsuffix [{default [so]} {target-winxp [dll]}]}}
    macro("shlibsuffix", (
      {"default": "so"},
      {"target-winxp": "dll"},
    ))
    #### macro &{{libdirname [{default [lib]}]}}
    macro("libdirname", (
      {"default": "lib"},
    ))
    #### macro &{{bindirname [{default [bin]}]}}
    macro("bindirname", (
      {"default": "bin"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
