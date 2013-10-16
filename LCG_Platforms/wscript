## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "LCG_Platforms",
    "authors": ["atlas collaboration"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## no public dependencies
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    tag = ctx.hwaf_declare_tag
    macro = ctx.hwaf_declare_macro
    
    ## Architectures ##
    tag("x86_64", content=["host-x86_64"])
    tag("i686",   content=["host-i686"])
    tag("i386",   content=["host-i386"])

    ## Compilers ##
    # gcc 3.4 series (latest release 3.4.6)
    tag("gcc340", content=["host-gcc34"])
    tag("gcc341", content=["host-gcc34"])
    tag("gcc342", content=["host-gcc34"])
    tag("gcc343", content=["host-gcc34"])
    tag("gcc344", content=["host-gcc34"])
    tag("gcc345", content=["host-gcc34"])
    tag("gcc346", content=["host-gcc34"])
    tag("gcc347", content=["host-gcc34"])
    tag("gcc348", content=["host-gcc34"])
    tag("host-gcc34", content=["host-gcc3"])
    
    # gcc 4.0 series (latest release 4.0.4)
    tag("gcc400", content=["host-gcc40"])
    tag("gcc401", content=["host-gcc40"])
    tag("gcc402", content=["host-gcc40"])
    tag("gcc403", content=["host-gcc40"])
    tag("gcc404", content=["host-gcc40"])
    tag("gcc405", content=["host-gcc40"])
    tag("gcc406", content=["host-gcc40"])
    tag("host-gcc40", content=["host-gcc4"])
    
    # gcc 4.1 series (latest release 4.1.2)
    tag("gcc410", content=["host-gcc41"])
    tag("gcc411", content=["host-gcc41"])
    tag("gcc412", content=["host-gcc41"])
    tag("gcc413", content=["host-gcc41"])
    tag("gcc414", content=["host-gcc41"])
    tag("host-gcc41", content=["host-gcc4"])
    
    # gcc 4.2 series (mainly for mac 10.6s gcc 4.2.1)
    tag("gcc420", content=["host-gcc42"])
    tag("gcc421", content=["host-gcc42"])
    tag("gcc422", content=["host-gcc42"])
    tag("gcc423", content=["host-gcc42"])
    tag("gcc424", content=["host-gcc42"])
    tag("host-gcc42", content=["host-gcc4"])
    
    # gcc 4.3 series (latest release 4.3.2)
    tag("gcc430", content=["host-gcc43"])
    tag("gcc431", content=["host-gcc43"])
    tag("gcc432", content=["host-gcc43"])
    tag("gcc433", content=["host-gcc43"])
    tag("gcc434", content=["host-gcc43"])
    tag("gcc435", content=["host-gcc43"])
    tag("gcc436", content=["host-gcc43"])
    tag("host-gcc43", content=["host-gcc4"])

    # gcc 4.4 series
    tag("gcc440", content=["host-gcc44"])
    tag("gcc441", content=["host-gcc44"])
    tag("gcc442", content=["host-gcc44"])
    tag("gcc443", content=["host-gcc44"])
    tag("gcc444", content=["host-gcc44"])
    tag("gcc445", content=["host-gcc44"])
    tag("gcc446", content=["host-gcc44"])
    tag("host-gcc44", content=["host-gcc4"])

    # gcc 4.5 series
    tag("gcc450", content=["host-gcc45"])
    tag("gcc451", content=["host-gcc45"])
    tag("gcc452", content=["host-gcc45"])
    tag("gcc453", content=["host-gcc45"])
    tag("gcc454", content=["host-gcc45"])
    tag("host-gcc45", content=["host-gcc4"])

    # gcc 4.6 series
    tag("gcc460", content=["host-gcc46"])
    tag("gcc461", content=["host-gcc46"])
    tag("gcc462", content=["host-gcc46"])
    tag("host-gcc46", content=["host-gcc4"])

    # gcc 4.7 series
    tag("gcc470", content=["host-gcc47"])
    tag("gcc471", content=["host-gcc47"])
    tag("host-gcc47", content=["host-gcc4"])

    # gcc 4.8 series
    tag("gcc480", content=["host-gcc48"])
    tag("gcc481", content=["host-gcc48"])
    tag("host-gcc48", content=["host-gcc4"])

    # Windows Visual Studio cl compiler
    tag("VisualC", content=["host-visualc"])
    tag("cl", content=["host-cl"])

    # further abstractions
    tag("host-gcc3", content=["host-gcc"])
    tag("host-gcc4", content=["host-gcc"])

    ## Operating systems ##
    tag("Linux", content=["host-linux"])
    tag("Darwin", content=["host-darwin"])
    tag("Unix", content=["host-unix"])
    tag("WIN32", content=["host-win7"])
    tag("XP", content=["host-winxp"])
    ## FIXME:
    # tag_exclude("host-winxp", content=["host-win7"])
    
    # slc4 series (latest release 4.7)
    tag("slc40", content=["host-slc4"])
    tag("slc41", content=["host-slc4"])
    tag("slc42", content=["host-slc4"])
    tag("slc43", content=["host-slc4"])
    tag("slc44", content=["host-slc4"])
    tag("slc45", content=["host-slc4"])
    tag("slc46", content=["host-slc4"])
    tag("slc47", content=["host-slc4"])
    tag("slc48", content=["host-slc4"])
    tag("slc49", content=["host-slc4"])
    # slc5 series (latest release 5.2)
    tag("slc50", content=["host-slc5"])
    tag("slc51", content=["host-slc5"])
    tag("slc52", content=["host-slc5"])
    tag("slc53", content=["host-slc5"])
    tag("slc54", content=["host-slc5"])
    tag("slc55", content=["host-slc5"])
    tag("slc56", content=["host-slc5"])
    tag("slc57", content=["host-slc5"])
    tag("slc58", content=["host-slc5"])
    tag("slc59", content=["host-slc5"])
    tag("slc510", content=["host-slc5"])
    # sl5 series (mapping it to slc5)
    tag("sl50", content=["host-slc5"])
    tag("sl51", content=["host-slc5"])
    tag("sl52", content=["host-slc5"])
    tag("sl53", content=["host-slc5"])
    tag("sl54", content=["host-slc5"])
    tag("sl55", content=["host-slc5"])
    tag("sl56", content=["host-slc5"])
    tag("sl57", content=["host-slc5"])
    tag("sl58", content=["host-slc5"])
    tag("sl59", content=["host-slc5"])
    tag("sl510", content=["host-slc5"])
    # slc6 series
    tag("slc60", content=["host-slc6"])
    tag("slc61", content=["host-slc6"])
    tag("slc62", content=["host-slc6"])
    tag("slc63", content=["host-slc6"])
    tag("slc64", content=["host-slc6"])
    tag("slc65", content=["host-slc6"])
    # rhel series
    tag("rhel60", content=["host-rhel6"])
    # further abstractions
    tag("host-slc4", content=["host-slc"])
    tag("host-slc5", content=["host-slc"])
    tag("host-slc6", content=["host-slc"])
    tag("host-rhel6", content=["host-rhel"])
    tag("host-slc", content=["host-linux"])
    tag("host-rhel", content=["host-linux"])
    tag("host-linux", content=["host-unix"])
    tag("host-darwin", content=["host-unix"])
    tag("host-winxp", content=["host-win"])
    tag("host-win7", content=["host-win"])

    # =====  Target Tags  =====

    # Common tags
    tag("i686-slc5-gcc34-opt", content=["target-i686", "target-slc5", "target-gcc34", "target-opt"])
    tag("i686-slc5-gcc34-dbg", content=["target-i686", "target-slc5", "target-gcc34", "target-dbg"])
    tag("i686-slc5-gcc41-opt", content=["target-i686", "target-slc5", "target-gcc41", "target-opt"])
    tag("i686-slc5-gcc41-dbg", content=["target-i686", "target-slc5", "target-gcc41", "target-dbg"])
    tag("i686-slc5-gcc43-opt", content=["target-i686", "target-slc5", "target-gcc43", "target-opt"])
    tag("i686-slc5-gcc43-dbg", content=["target-i686", "target-slc5", "target-gcc43", "target-dbg"])
    tag("i686-slc5-gcc44-opt", content=["target-i686", "target-slc5", "target-gcc44", "target-opt"])
    tag("i686-slc5-gcc44-dbg", content=["target-i686", "target-slc5", "target-gcc44", "target-dbg"])
    tag("i686-slc5-gcc45-opt", content=["target-i686", "target-slc5", "target-gcc45", "target-opt"])
    tag("i686-slc5-gcc45-dbg", content=["target-i686", "target-slc5", "target-gcc45", "target-dbg"])
    tag("i686-slc5-gcc46-opt", content=["target-i686", "target-slc5", "target-gcc46", "target-opt"])
    tag("i686-slc5-gcc46-dbg", content=["target-i686", "target-slc5", "target-gcc46", "target-dbg"])
    tag("i686-slc5-gcc47-opt", content=["target-i686", "target-slc5", "target-gcc47", "target-opt"])
    tag("i686-slc5-gcc47-dbg", content=["target-i686", "target-slc5", "target-gcc47", "target-dbg"])
    tag("i686-slc5-gccmax-opt", content=["target-i686", "target-slc5", "target-gccmax", "target-opt"])
    tag("i686-slc5-gccmax-dbg", content=["target-i686", "target-slc5", "target-gccmax", "target-dbg"])
    tag("i686-slc5-g11max-opt", content=["target-i686", "target-slc5", "target-g11max", "target-opt"])
    tag("i686-slc5-g11max-dbg", content=["target-i686", "target-slc5", "target-g11max", "target-dbg"])
    tag("x86_64-slc5-gcc34-opt", content=["target-x86_64", "target-slc5", "target-gcc34", "target-opt"])
    tag("x86_64-slc5-gcc34-dbg", content=["target-x86_64", "target-slc5", "target-gcc34", "target-dbg"])
    tag("x86_64-slc5-gcc41-opt", content=["target-x86_64", "target-slc5", "target-gcc41", "target-opt"])
    tag("x86_64-slc5-gcc41-dbg", content=["target-x86_64", "target-slc5", "target-gcc41", "target-dbg"])
    tag("x86_64-slc5-gcc43-opt", content=["target-x86_64", "target-slc5", "target-gcc43", "target-opt"])
    tag("x86_64-slc5-gcc43-dbg", content=["target-x86_64", "target-slc5", "target-gcc43", "target-dbg"])
    tag("x86_64-slc5-gcc44-opt", content=["target-x86_64", "target-slc5", "target-gcc44", "target-opt"])
    tag("x86_64-slc5-gcc44-dbg", content=["target-x86_64", "target-slc5", "target-gcc44", "target-dbg"])
    tag("x86_64-slc5-gcc45-opt", content=["target-x86_64", "target-slc5", "target-gcc45", "target-opt"])
    tag("x86_64-slc5-gcc45-dbg", content=["target-x86_64", "target-slc5", "target-gcc45", "target-dbg"])
    tag("x86_64-slc5-gcc46-opt", content=["target-x86_64", "target-slc5", "target-gcc46", "target-opt"])
    tag("x86_64-slc5-gcc46-dbg", content=["target-x86_64", "target-slc5", "target-gcc46", "target-dbg"])
    tag("x86_64-slc5-gcc47-opt", content=["target-x86_64", "target-slc5", "target-gcc47", "target-opt"])
    tag("x86_64-slc5-gcc47-dbg", content=["target-x86_64", "target-slc5", "target-gcc47", "target-dbg"])
    tag("x86_64-slc5-gccmax-opt", content=["target-x86_64", "target-slc5", "target-gccmax", "target-opt"])
    tag("x86_64-slc5-gccmax-dbg", content=["target-x86_64", "target-slc5", "target-gccmax", "target-dbg"])
    tag("x86_64-slc5-g11max-opt", content=["target-x86_64", "target-slc5", "target-g11max", "target-opt"])
    tag("x86_64-slc5-g11max-dbg", content=["target-x86_64", "target-slc5", "target-g11max", "target-dbg"])
    tag("x86_64-slc5-clang31-opt", content=["target-x86_64", "target-slc5", "target-clang31", "target-opt"])
    tag("x86_64-slc5-clang31-dbg", content=["target-x86_64", "target-slc5", "target-clang31", "target-dbg"])
    tag("i686-slc6-gcc44-opt", content=["target-i686", "target-slc6", "target-gcc44", "target-opt"])
    tag("i686-slc6-gcc44-dbg", content=["target-i686", "target-slc6", "target-gcc44", "target-dbg"])
    tag("i686-slc6-gcc45-opt", content=["target-i686", "target-slc6", "target-gcc45", "target-opt"])
    tag("i686-slc6-gcc45-dbg", content=["target-i686", "target-slc6", "target-gcc45", "target-dbg"])
    tag("i686-slc6-gcc46-opt", content=["target-i686", "target-slc6", "target-gcc46", "target-opt"])
    tag("i686-slc6-gcc46-dbg", content=["target-i686", "target-slc6", "target-gcc46", "target-dbg"])
    tag("i686-slc6-gcc47-opt", content=["target-i686", "target-slc6", "target-gcc47", "target-opt"])
    tag("i686-slc6-gcc47-dbg", content=["target-i686", "target-slc6", "target-gcc47", "target-dbg"])
    tag("i686-slc6-gccmax-opt", content=["target-i686", "target-slc6", "target-gccmax", "target-opt"])
    tag("i686-slc6-gccmax-dbg", content=["target-i686", "target-slc6", "target-gccmax", "target-dbg"])
    tag("i686-slc6-g11max-opt", content=["target-i686", "target-slc6", "target-g11max", "target-opt"])
    tag("i686-slc6-g11max-dbg", content=["target-i686", "target-slc6", "target-g11max", "target-dbg"])
    tag("x86_64-slc6-gcc44-opt", content=["target-x86_64", "target-slc6", "target-gcc44", "target-opt"])
    tag("x86_64-slc6-gcc44-dbg", content=["target-x86_64", "target-slc6", "target-gcc44", "target-dbg"])
    tag("x86_64-slc6-gcc45-opt", content=["target-x86_64", "target-slc6", "target-gcc45", "target-opt"])
    tag("x86_64-slc6-gcc45-dbg", content=["target-x86_64", "target-slc6", "target-gcc45", "target-dbg"])
    tag("x86_64-slc6-gcc46-opt", content=["target-x86_64", "target-slc6", "target-gcc46", "target-opt"])
    tag("x86_64-slc6-gcc46-dbg", content=["target-x86_64", "target-slc6", "target-gcc46", "target-dbg"])
    tag("x86_64-slc6-gcc47-opt", content=["target-x86_64", "target-slc6", "target-gcc47", "target-opt"])
    tag("x86_64-slc6-gcc47-dbg", content=["target-x86_64", "target-slc6", "target-gcc47", "target-dbg"])
    tag("x86_64-slc6-gcc48-opt", content=["target-x86_64", "target-slc6", "target-gcc48", "target-opt"])
    tag("x86_64-slc6-gcc48-dbg", content=["target-x86_64", "target-slc6", "target-gcc48", "target-dbg"])
    tag("x86_64-slc6-gccmax-opt", content=["target-x86_64", "target-slc6", "target-gccmax", "target-opt"])
    tag("x86_64-slc6-gccmax-dbg", content=["target-x86_64", "target-slc6", "target-gccmax", "target-dbg"])
    tag("x86_64-slc6-g11max-opt", content=["target-x86_64", "target-slc6", "target-g11max", "target-opt"])
    tag("x86_64-slc6-g11max-dbg", content=["target-x86_64", "target-slc6", "target-g11max", "target-dbg"])
    tag("x86_64-slc6-clang30-opt", content=["target-x86_64", "target-slc6", "target-clang30", "target-opt"])
    tag("x86_64-slc6-clang30-dbg", content=["target-x86_64", "target-slc6", "target-clang30", "target-dbg"])
    tag("x86_64-slc6-clang31-opt", content=["target-x86_64", "target-slc6", "target-clang31", "target-opt"])
    tag("x86_64-slc6-clang31-dbg", content=["target-x86_64", "target-slc6", "target-clang31", "target-dbg"])
    tag("i386-mac106-gcc42-dbg", content=["target-i386", "target-mac106", "target-gcc42", "target-dbg"])
    tag("i386-mac106-gcc42-opt", content=["target-i386", "target-mac106", "target-gcc42", "target-opt"])
    tag("i386-mac107-gcc42-dbg", content=["target-i386", "target-mac107", "target-gcc42", "target-dbg"])
    tag("i386-mac107-gcc42-opt", content=["target-i386", "target-mac107", "target-gcc42", "target-opt"])
    tag("i386-mac108-gcc42-dbg", content=["target-i386", "target-mac108", "target-gcc42", "target-dbg"])
    tag("i386-mac108-gcc42-opt", content=["target-i386", "target-mac108", "target-gcc42", "target-opt"])
    tag("x86_64-mac106-gcc42-dbg", content=["target-x86_64", "target-mac106", "target-gcc42", "target-dbg"])
    tag("x86_64-mac106-gcc42-opt", content=["target-x86_64", "target-mac106", "target-gcc42", "target-opt"])
    tag("x86_64-mac107-gcc42-dbg", content=["target-x86_64", "target-mac107", "target-gcc42", "target-dbg"])
    tag("x86_64-mac107-gcc42-opt", content=["target-x86_64", "target-mac107", "target-gcc42", "target-opt"])
    tag("x86_64-mac108-gcc42-dbg", content=["target-x86_64", "target-mac108", "target-gcc42", "target-dbg"])
    tag("x86_64-mac108-gcc42-opt", content=["target-x86_64", "target-mac108", "target-gcc42", "target-opt"])
    tag("i686-winxp-vc9-opt", content=["target-i686", "target-winxp", "target-vc9", "target-opt"])
    tag("i686-winxp-vc9-dbg", content=["target-i686", "target-winxp", "target-vc9", "target-dbg"])
    tag("i686-win7-vc9-opt", content=["target-i686", "target-win7", "target-vc9", "target-opt"])
    tag("i686-win7-vc9-dbg", content=["target-i686", "target-win7", "target-vc9", "target-dbg"])
    tag("x86_64-win7-vc9-opt", content=["target-x86_64", "target-win7", "target-vc9", "target-opt"])
    tag("x86_64-win7-vc9-dbg", content=["target-x86_64", "target-win7", "target-vc9", "target-dbg"])

    # Common testing tags (i.e. not foreseen to be used for release)
    tag("i686-slc5-icc11-opt", content=["target-i686", "target-slc5", "target-icc11", "target-opt"])
    tag("i686-slc5-icc11-dbg", content=["target-i686", "target-slc5", "target-icc11", "target-dbg"])
    tag("x86_64-slc5-icc11-opt", content=["target-x86_64", "target-slc5", "target-icc11", "target-opt"])
    tag("x86_64-slc5-icc11-dbg", content=["target-x86_64", "target-slc5", "target-icc11", "target-dbg"])
    tag("slc4_amd64_gcc43_cov", content=["target-x86_64", "target-slc4", "target-gcc43", "target-cov"])
    tag("x86_64-slc5-gcc43-cov", content=["target-x86_64", "target-slc5", "target-gcc43", "target-cov"])
    tag("x86_64-rhel6-gcc44-opt", content=["target-x86_64", "target-rhel6", "target-gcc44", "target-opt"])
    tag("x86_64-rhel6-gcc44-dbg", content=["target-x86_64", "target-rhel6", "target-gcc44", "target-dbg"])
    tag("x86_64-slc5-gcc43-pro", content=["target-x86_64", "target-slc5", "target-gcc43", "target-pro"])

    # ATLAS CMTCONFIG tags
    tag("x86_64-slc4-gcc34-opt", content=["target-x86_64", "target-slc4", "target-gcc34", "target-opt"])
    tag("x86_64-slc4-gcc34-dbg", content=["target-x86_64", "target-slc4", "target-gcc34", "target-dbg"])
    tag("x86_64-slc4-gcc41-opt", content=["target-x86_64", "target-slc4", "target-gcc41", "target-opt"])
    tag("x86_64-slc4-gcc41-dbg", content=["target-x86_64", "target-slc4", "target-gcc41", "target-dbg"])
    tag("x86_64-slc4-gcc43-opt", content=["target-x86_64", "target-slc4", "target-gcc43", "target-opt"])
    tag("x86_64-slc4-gcc43-dbg", content=["target-x86_64", "target-slc4", "target-gcc43", "target-dbg"])
    tag("i686-slc4-gcc34-opt", content=["target-i686", "target-slc4", "target-gcc34", "target-opt"])
    tag("i686-slc4-gcc34-dbg", content=["target-i686", "target-slc4", "target-gcc34", "target-dbg"])
    tag("i686-slc4-gcc41-opt", content=["target-i686", "target-slc4", "target-gcc34", "target-opt"])
    tag("i686-slc4-gcc41-dbg", content=["target-i686", "target-slc4", "target-gcc34", "target-dbg"])
    tag("i686-slc4-gcc43-opt", content=["target-i686", "target-slc4", "target-gcc43", "target-opt"])
    tag("i686-slc4-gcc43-dbg", content=["target-i686", "target-slc4", "target-gcc43", "target-dbg"])
    tag("i386-mac105-gcc40-dbg", content=["target-i386", "target-mac105", "target-gcc40", "target-dbg"])
    tag("i386-mac105-gcc40-opt", content=["target-i386", "target-mac105", "target-gcc40", "target-opt"])

    # LHCb CMTCONFIG tags
    tag("slc4_amd64_gcc34", content=["target-x86_64", "target-slc4", "target-gcc34", "target-opt"])
    tag("slc4_amd64_gcc34_dbg", content=["target-x86_64", "target-slc4", "target-gcc34", "target-dbg"])
    tag("slc4_amd64_gcc41", content=["target-x86_64", "target-slc4", "target-gcc41", "target-opt"])
    tag("slc4_amd64_gcc41_dbg", content=["target-x86_64", "target-slc4", "target-gcc41", "target-dbg"])
    tag("slc4_amd64_gcc43", content=["target-x86_64", "target-slc4", "target-gcc43", "target-opt"])
    tag("slc4_amd64_gcc43_dbg", content=["target-x86_64", "target-slc4", "target-gcc43", "target-dbg"])
    tag("slc4_ia32_gcc34", content=["target-i686", "target-slc4", "target-gcc34", "target-opt"])
    tag("slc4_ia32_gcc34_dbg", content=["target-i686", "target-slc4", "target-gcc34", "target-dbg"])
    tag("slc4_ia32_gcc41", content=["target-i686", "target-slc4", "target-gcc41", "target-opt"])
    tag("slc4_ia32_gcc41_dbg", content=["target-i686", "target-slc4", "target-gcc41", "target-dbg"])
    tag("slc4_ia32_gcc43", content=["target-i686", "target-slc4", "target-gcc43", "target-opt"])
    tag("slc4_ia32_gcc43_dbg", content=["target-i686", "target-slc4", "target-gcc43", "target-dbg"])
    tag("osx105_ia32_gcc401", content=["target-i386", "target-mac105", "target-gcc40", "target-opt"])
    tag("osx105_ia32_gcc401_dbg", content=["target-i386", "target-mac105", "target-gcc40", "target-dbg"])
    tag("win32_vc71", content=["target-i686", "target-winxp", "target-vc71", "target-opt"])
    tag("win32_vc71_dbg", content=["target-i686", "target-winxp", "target-vc71", "target-dbg"])

    # further abstractions
    tag("target-slc4", content=["target-slc"])
    tag("target-slc5", content=["target-slc"])
    tag("target-slc6", content=["target-slc"])
    tag("target-slc", content=["target-linux"])
    tag("target-rhel6", content=["target-rhel"])
    tag("target-rhel", content=["target-linux"])
    tag("target-linux", content=["target-unix"])
    tag("target-mac105", content=["target-mac"])
    tag("target-mac106", content=["target-mac"])
    tag("target-mac107", content=["target-mac"])
    tag("target-mac108", content=["target-mac"])
    tag("target-mac", content=["target-darwin"])
    tag("target-darwin", content=["target-unix"])
    tag("target-winxp", content=["target-win"])
    tag("target-win7", content=["target-win"])
    
    tag("target-gcc34", content=["target-gcc3"])
    tag("target-gcc40", content=["target-gcc4"])
    tag("target-gcc41", content=["target-gcc4"])
    tag("target-gcc42", content=["target-gcc4"])
    tag("target-gcc43", content=["target-gcc4", "target-lcg-compiler", "lcg-compiler"])
    tag("target-gcc44", content=["target-gcc4"])
    tag("target-gcc45", content=["target-gcc4", "target-lcg-compiler", "lcg-compiler"])
    tag("target-gcc46", content=["target-gcc4", "target-lcg-compiler", "lcg-compiler"])
    tag("target-gcc47", content=["target-gcc4", "target-lcg-compiler", "lcg-compiler", "target-c11"])
    tag("target-gcc48", content=["target-gcc4", "target-lcg-compiler", "lcg-compiler", "target-c11"])
    tag("target-gccmax", content=["target-gcc4", "target-lcg-compiler", "lcg-compiler"])
    tag("target-g11max", content=["target-gcc4", "target-lcg-compiler", "lcg-compiler", "target-c11"])
    tag("target-clang30", content=["target-clang3"])
    tag("target-clang31", content=["target-clang3"])
    
    tag("target-gcc3", content=["target-gcc"])
    tag("target-gcc4", content=["target-gcc"])
    tag("target-icc11", content=["target-icc"])
    tag("target-clang3", content=["target-clang", "target-llvm"])
    
    tag("target-vc71", content=["target-vc7"])
    tag("target-vc7", content=["target-vc"])
    tag("target-vc9", content=["target-vc"])

    # =====  LCG_system + LCG_platform  =====
    
    # which gcc version will work with a given icc, clang, ... compiler
    # Any change to macro gcc2icc should also be reflected in LCG_Setting
    # macro gcc_config_version which we need for setting up LD_LIBRARY_PATH
    # to pick up e.g. the right libstdc++.so.x.y.z from afs if necessary
    macro("gcc2icc", (
        {"default": ""},
        {"target-icc11": "gcc43"},
    ))
    macro("gcc2clang", (
      {"default": ""},
      {"target-clang3": "gcc46"},
    ))
    macro("gcc2max", (
      {"default": ""},
      {"target-gccmax": "gcc46"},
    ))
    macro("gcc2g11", (
      {"default": ""},
      {"target-g11max": "gcc46"},
    ))

    macro("LCG_arch", (
      {"default": ""},
      {"target-x86_64": "x86_64"},
      {"target-i686": "i686"},
      {"target-i386": "i386"},
      {("target-slc4", "target-x86_64"): "amd64"},
      {("target-slc4", "target-i686"): "ia32"},
      {"target-mac105": "ia32"},
    ))

    macro("LCG_os", (
      {"default": ""},
      {"target-slc6": "slc6"},
      {"target-slc5": "slc5"},
      {"target-slc4": "slc4"},
      {"target-mac108": "mac108"},
      {"target-mac107": "mac107"},
      {"target-mac106": "mac106"},
      {"target-mac105": "osx105"},
      {"target-win7": "win7"},
      {"target-winxp": "winxp"},
    ))

    macro("LCG_compiler", (
      {"default": ""},
      {"target-gcc34": "gcc34"},
      {"target-gcc40": "gcc401"},
      {"target-gcc41": "gcc41"},
      {"target-gcc42": "gcc42"},
      {"target-gcc43": "gcc43"},
      {"target-gcc44": "gcc44"},
      {"target-gcc45": "gcc45"},
      {"target-gcc46": "gcc46"},
      {"target-gcc47": "gcc47"},
      {"target-gcc48": "gcc48"},
      {"target-gccmax": "gccmax"},
      {"target-g11max": "g11max"},
      {"target-icc11": "icc11"},
      {"target-icc12": "icc12"},
      {"target-clang30": "clang30"},
      {"target-clang31": "clang31"},
      {"target-vc71": "vc71"},
      {"target-vc9": "vc9"},
    ))

    macro("LCG_mode", (
      {"default": "opt"},
      {"target-dbg": "dbg"},
      {"target-cov": "cov"},
      {"target-pro": "pro"},
    ))

    macro("LCG_basesystem", (
      {"default": "${LCG_arch}-${LCG_os}-${LCG_compiler}"},
      {"target-slc4": "${LCG_os}_${LCG_arch}_${LCG_compiler}"},
      {"target-mac105": "${LCG_os}_${LCG_arch}_${LCG_compiler}"},
      {"target-vc71": "win32_vc71"},
    ))

    macro("LCG_system", (
      {"default": "${LCG_basesystem}-opt"},
      {"target-clang": "${LCG_arch}-${LCG_os}-${gcc2clang}-opt"},
      {"target-icc11": "${LCG_arch}-${LCG_os}-${gcc2icc}-opt"},
      {"target-gccmax": "${LCG_arch}-${LCG_os}-${gcc2max}-opt"},
      {"target-g11max": "${LCG_arch}-${LCG_os}-${gcc2g11}-opt"},
      {"target-slc4": "${LCG_basesystem}"},
      {"target-mac105": "${LCG_basesystem}"},
      {"target-vc71": "${LCG_basesystem}"},
    ))

    macro("LCG_platform", (
      {"default": "${LCG_basesystem}-${LCG_mode}"},
      {("target-dbg", "target-slc4"): "${LCG_basesystem}_dbg"},
      {("target-dbg", "target-mac105"): "${LCG_basesystem}_dbg"},
      {("target-dbg", "target-vc71"): "${LCG_basesystem}_dbg"},
      {"target-slc4": "${LCG_basesystem}"},
      {"target-mac105": "${LCG_basesystem}"},
      {"target-vc71": "${LCG_basesystem}"},
    ))
    # FIXME: set statement
    ##### **** statement *hlib.SetStmt (&{{ATLAS_TAGS_MAP [{default [none]} {slc4_ia32_gcc34 [i686-slc4-gcc34-opt]} {slc4_ia32_gcc34_dbg [i686-slc4-gcc34-dbg]} {slc4_ia32_gcc41 [i686-slc4-gcc41-opt]} {slc4_ia32_gcc41_dbg [i686-slc4-gcc41-dbg]} {slc4_ia32_gcc43 [i686-slc4-gcc43-opt]} {slc4_ia32_gcc43_dbg [i686-slc4-gcc43-dbg]} {slc4_amd64_gcc34 [x86_64-slc4-gcc34-opt]} {slc4_amd64_gcc34_dbg [x86_64-slc4-gcc34-dbg]} {slc4_amd64_gcc41 [x86_64-slc4-gcc41-opt]} {slc4_amd64_gcc41_dbg [x86_64-slc4-gcc41-dbg]} {slc4_amd64_gcc43 [x86_64-slc4-gcc43-opt]} {slc4_amd64_gcc43_dbg [x86_64-slc4-gcc43-dbg]} {osx105_ia32_gcc401 [i386-mac105-gcc40-opt]} {osx105_ia32_gcc401_dbg [i386-mac105-gcc40-dbg]}]}})

    # =====  Automatic setup of CMTCONFIG  =====

    macro("host_compiler", (
      {"default": "UnknownCompiler"},
      {"host-slc6": "gcc44"},
      {"host-slc5": "gcc43"},
      {"host-slc4": "gcc34"},
      {"host-gcc34": "gcc34"},
      {"host-gcc40": "gcc40"},
      {"host-gcc41": "gcc41"},
      {"host-gcc42": "gcc42"},
      {"host-gcc43": "gcc43"},
      {"host-gcc44": "gcc44"},
      {"host-gcc45": "gcc45"},
      {"host-gcc46": "gcc46"},
      {"host-gcc": "unknownGcc"},
      {"host-clang30": "clang30"},
      {"host-clang31": "clang31"},
      {"host-clang": "unknownClang"},
      {"host-icc11": "icc11"},
      {"host-icc": "unknownIcc"},
    ))

    macro("host_arch", (
      {"default": "UnknownArch"},
      {("host-darwin", "host-i386", "host-gcc40"): "ia32"},
      {("host-slc4", "host-x86_64"): "amd64"},
      {("host-slc4", "host-i686"): "ia32"},
      {"host-x86_64": "x86_64"},
      {"host-i686": "i686"},
      {"host-i386": "i386"},
      {"host-ppc": "ppc"},
    ))

    macro("host_os", (
      {"default": "UnknownOS"},
      {"host-slc4": "slc4"},
      {"host-slc5": "slc5"},
      {"host-slc6": "slc6"},
      {"host-debian": "debian"},
      {"host-linux": "linux"},
      {("host-darwin", "host-gcc40"): "osx104"},
      {"host-darwin": "darwin"},
    ))

    # FIXME: set statement
    ##### **** statement *hlib.SetStmt (&{{host_cmtconfig [{default [${host_arch}-${host_os}-${host_compiler}-opt]} {host-slc4 [${host_os}_${host_arch}_${host_compiler}]} {host-darwin&host-gcc40 [${host_os}_${host_arch}_${host_compiler}]} {host-win&target-vc7 [win32_vc71_dbg]}]}})
    macro("host_cmtconfig", (
        {"default": "${host_arch}-${host_os}-${host_compiler}-opt"},
        {"host-slc4": "${host_os}_${host_arch}_${host_compiler}"},
        {("host-darwin","host-gcc40"): "${host_os}_${host_arch}_${host_compiler}"},
        {("host-win", "target-vc7"): "win32_vc71_dbg"}
        ))
    ctx.hwaf_declare_runtime_env("host_cmtconfig")
    
    macro("LCG_hostos", (
      {"default": "${host_arch}-${LCG_os}"},
      {"host-slc6": "${host_arch}-${host_os}"},
      {"host-slc5": "${host_arch}-${host_os}"},
      {"host-slc4": "${host_arch}-${host_os}"},
    ))

    macro("LCG_hostarch", (
      {"default": "${host_arch}"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
