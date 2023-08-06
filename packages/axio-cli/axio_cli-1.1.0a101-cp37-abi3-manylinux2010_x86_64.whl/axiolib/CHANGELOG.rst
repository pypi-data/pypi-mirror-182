
Change Log
==========

1.1.0-a.101 <2022-12-18>
-----------------------

New features
~~~~~~~~~~~~

Bugfixes
~~~~~~~~

    * the cpp framework specified in aworks lp framework cannot be automatically downloaded

Incompatible
~~~~~~~~~~~~

1.1.0-a.100 <2022-11-28>
-----------------------

New features
~~~~~~~~~~~~

    * add aworks solution axbuilder test case

Bugfixes
~~~~~~~~
    
    * fixed a bug that ignores is not working in dist buildfiles
    * fixed a bug where solution builder was not imported when use package inheritance
    * fixed a bug where changelog and readme was not registered when publish the packages for the production stage
    * fixed a bug that when component exist depencies loop will build fail

Incompatible
~~~~~~~~~~~~

1.1.0-a.99 <2022-11-20>
-----------------------

New features
~~~~~~~~~~~~

Bugfixes
~~~~~~~~

    * ComponentBuilder: fixed validation board failure when the platform is None

Incompatible
~~~~~~~~~~~~

1.1.0-a.98 <2022-10-9>
-----------------------

New features
~~~~~~~~~~~~
    
    * add properties to the interface of solution to get data
    * FrameworkCpp: split the framework cpp into separate framework
    * SolutionBuilder: split the solution into separate component
    * ComponentBase: add define(macro) of version to defines for component
    * process buildset from get_buildset_for_self() while building program
    * RstdocBuilder: print information of doc's dependencies(frameworks, components...)
    * add support for `subframework`

Bugfixes
~~~~~~~~
    
    * fixed build_cpp_artifact still running while ``build -tsdist``
    * fixed build_xdist option `datafiles` is invalid when build python exe
    * fixed an bug with incorrect environment variables during CI generation
    * fixed ubuntu16 runner to build
    * fix wrong tips: packaging version different with commit tag can be bypass via --disable-ci-check <- this is not allowed
    * fix bug: CI test stage may download incorrect previous stage packages
    * fix TCL_LIBRARY and TK_LIBRARY in os.environ for linux

Incompatible
~~~~~~~~~~~~

1.1.0-a.97 <2022-9-9>
-----------------------

New features
~~~~~~~~~~~~

    * add a tutorial for setting up a development environment for Linux

Bugfixes
~~~~~~~~

    * CI does not check the version number in test mode
    * symbolic links cannot be set with permissions on Linux

Incompatible
~~~~~~~~~~~~

1.1.0-a.96 <2022-8-11>
-----------------------

New features
~~~~~~~~~~~~
    
    * add toolchains: ``gcc`` and ``gcc-cross`` for inherit
    * add options: ``artifact_type`` and ``artifact_name``
    * support to upload static web document to outer network AXPI
    * add option ``skip_process_config`` for skip process config while building cpp artifact
    * add option ``skip_construct`` for skip constrcut while building cpp artifact
    * add option ``dist_buildfiles`` for dist files in build directory
    * enable ``auto_coerce`` in _normalize_schema as default
    * ComponentBuilder : add ``build_xdist_components`` for xdist other components
    * add `DynamicProxyBase` to increase indexing loading speed
    * enable axpi repo test
    * solutions support products that build application type
    * `venv_cmd.bat venv_git_bash.bat` startup scripts don't gain administrator permission
    * when used in the IDE, copy the framework and platform to the `.axiodeps` directory
    * when used in the IDE, link the framework and platform to the `.axiodeps` directory

Bugfixes
~~~~~~~~

    * can't delete source files when rename fail
    * fix a bug that internet cannot be connected in the outer net environment
    * fix a bug where version properties do not take effect in the solution configuration
    * axprj: axio-cli will raise a error when open a invalid project
    * link fail when build application which using armcc, due to _LIBFLAGS without .lib .
    * pkg_cls.__module__ not set mod_path lead to Builder reload abnormal.
    * individual builder can not inherit correctly

Incompatible
~~~~~~~~~~~~

1.1.0-a.95 <2022-7-26>
-----------------------

New features
~~~~~~~~~~~~
    
    * utils: add some methods ``create_junction`` ``is_junction`` ``unlink_junction`` in order to replace symbolic links
    * add prompting message in kconfig for interface relationship
    * support to create symlink of directory when don't have admin permission
    * add rstdoc ui schema configuration
    * ComponentBase: add method ``get_buildset_for_self()``
    * Deparser： add method ``process_dependencies()``
    * DepNode: add method ``get_ldf_mode()``

Bugfixes
~~~~~~~~

    * fix the bug that the `os.path.islink` function cannot recognize the junction point
    * remove individual controversial parameters(`dependencies` in rstdoc)
    * fix nuitka `CCACHE` file error when nuitka build
    * fix error in parse artifact_type for dependencies

Incompatible
~~~~~~~~~~~~

1.1.0-a.94 <2022-7-25>
-----------------------

New features
~~~~~~~~~~~~
     
    * ToolchainBase: add method ``parse_flag`` for parse special flags in toolchain

Bugfixes
~~~~~~~~

    * Deparser: the build fails when build set is `*`
    * RstdocBuilder : fix error while register doc product because of ``same identifier`` in env.AxClone
    * Component: Dependencies deal in DepNode, but not set _is_dependent in pkgobj

Incompatible
~~~~~~~~~~~~

1.1.0-a.93 <2022-5-30>
-----------------------

New features
~~~~~~~~~~~~

    * upload component of `sdist` type to solution directory
    * throw error when config a invalid solution
    * upgrade `Nuitka` version to `0.9.3`
    * optimize the logic for registering test reports
    * improve support shared library, add build options ``dep_shlib_link`` and ``dep_artifact_type``
    * improve the directory structure of the solution
    * add `packaging_manifest` for custom manifest
    * RstdocBuilder : update to use package ``venv-rstdoc-win-py3@^1.3.0``

Bugfixes
~~~~~~~~

    * generate a ci script of application will fail
    * a leading zero in version can cause errors
    * too much time is spent loading invalid project
    * the `os.path.exists` `os.path.isfile` function still returns true when the suffix "\" is added to the file path on a Huawei computer
    * when the svn command operation fails, the print message contains the user name and password
    * fixed the issue that when there is no permission for partial dist components, the application project configured with the solution can also be built normally
    * dist type components if they do not exist src_dir parameters may cause errors during compilation

Incompatible
~~~~~~~~~~~~

1.1.0-a.92 <2022-5-25>
-----------------------

New features
~~~~~~~~~~~~
    
    * record solution version information in a frozen file，probe solutions compared to recorded versions in frozen files
    * Repo : separate axpi client and repository-related code
    * AxbuilderBuildMixin : clear MEMORY_CACHE in PkgInstallerMixin
    * FrameworkCpp : improve ``get_src_dir`` and ``get_src_filter`` in ``CppApplication`` for support custom src_dir and src_filter

    * Repo:

        - register for automated test reports generated by axio-cli
        - add the interfaces for the registration report
        - add axpi package repo of public network
        - improve `AxpiPackageRepo` axpi package repo

    * PlatformBase : install share libs(.dll, .so) for application
    * CppComponentBuilde : normalized the filename of .config and .lockconfig
    * Toolchian gcc-mingw32 : add tool ``mingw`` to DEFAULT_TOOLS
    * RstdocBuilder : always prepare package ``tool-miktex``, other targets still need tool-miktex for math
    * set the expanduser to True for extra_*_dirs/adds in project configuration
    * improve ``util.Sysenv()`` : make sure the id(os.environ) do not change
    * new unified decompressing tool added: axio.unpacker.FileUnpacker and env.AxArchive() , support gz bz2 7z zip etc.
    * generating system first added
    * Package Manager: add common way to add inner packages and options to ignore them
    * `axio.__version__` always grab from package.json
    * improve ``util.match_files()`` : fully support ignore via .gitignore and support pick up symbol links
    * improve ``env.AxCollectBuildFiles()`` : better way to process src files outside `src_dir`
    * srcobj can be decided via 'ci.source' or 'develop.source'
    * support use glob pattern to specify manual ci jobs via ci.manual_jobs opt.

Bugfixes
~~~~~~~~

    * if the report is empty, deregistration will fail
    * register report will fail when publish package
    * the internal index is missing from the manifest of the solution
    * fixed an issue where switching working directories in the multithreaded 7z tool caused the solution to fail to build
    * prompts permission issues when loading manifest after downloading the package in Linux. Workaround: After the package download is complete, recursively set permissions for the files inside the package.
    * there is a place in the function that judges islink in Python2 that is designed to convert the path to the unicode type, and if the path contains gbk encoding, the conversion will fail. Workaround: Try decode(gbk) after the first conversion fails.
    * when the solution compresses 7z in python2, if the path in the _list.txt has a Chinese, the default encoding method Chinese use gbk, and 7z will prompt an encoding error when executing the compression command. Workaround: Resolve the issue after converting to UTF-8.
    * an issue where the build may fail after the repository is split.
    * FrameworkCpp : KconfigMenu.get_kconfig_string() will return error string while sort is False 
    * RstdocBuilder : sphinx will run fail while path with whitespaces
    * register a solution will fail
    * remove `src_dir` from a manifest of dist component
    * build solution when use 7z format will fail
    * build the platform of sdist distribution type in solution will fail
    * TCL_LIBRARY and TK_LIBRARY in os.environ not set correctly for linux_x86_64
    * `ignore` configuration is invalid when build a solution
    * solve a issue of chinese encoding error of unzipped file under Windows system
    * svn commit too many the files will fail
    * modify the site of temporary directory
    * fix __version__ encoding error in python2


Incompatible
~~~~~~~~~~~~

1.1.0-a.91 <2022-3-10>
-----------------------

New features
~~~~~~~~~~~~

    * Toolchain Class can be overrode by Toolchain Package and Platform
    * The default value of ``enable_long_paths`` (in AXIO Project configuration) is set to true
    * improve ``AxPreparePackage`` to support package dir
    * improve the toochain settings of msvc
    * improve build sharedlibrary to support component with dependency

Bugfixes
~~~~~~~~

    * store the package information in the solution to the frozen file
    * fix the types of schema, set `variables` property will throw `ValidationError`
    * fix bug: '!#' git-version will lead component compatible check fail.
    * fix the property 'packages' in BuilderBase
    
Incompatible
~~~~~~~~~~~~

1.1.0-a.90 <2022-2-15>
-----------------------

New features
~~~~~~~~~~~~


Bugfixes
~~~~~~~~

    * worker running will fail under python3
    * worker test cases running instability
    * worker running will fail under python3
    * `axio ci freeze` incorrectly switched to the last frozen engine version.


Incompatible
~~~~~~~~~~~~


1.1.0-a.89 <2021-12-31>
-----------------------

New features
~~~~~~~~~~~~

    * Build System:

        - C/CPP: support undefine by put a ``!`` in front of define

    * Builders:

        - RstdocBuilder: updated to support sphinx 4.3.1

    * Frameworks:

        - new framework ``cpp`` added for support basic C/CPP building

    * Toolchains:

        - new toolchain ``gcc-mingw64``

Bugfixes
~~~~~~~~

    * trigger worker will fail under python3
    * sync the html files of rst document will fail under python3
    * fixup the missing `axbuild markers` definitions

Incompatible
~~~~~~~~~~~~


1.1.0-a.88 <2021-12-10>
-----------------------

New features
~~~~~~~~~~~~

    * Builders:

        - improve the output content of target of ``idedata``
        - add ui configurations to schemas for builders

Bugfixes
~~~~~~~~

    * build rst document will to throw `AttributeError: disable_autocopy`
    * build solution will to throw `StopIteration` exception under python3
    * publish a package of platform category will to throw `StopIteration` exception
    * `RstdocBuilder` : ``-tautopreview`` will not work if python.exe path contain spaces
    * `axio ci init` will fail if build option `system` is list type

Incompatible
~~~~~~~~~~~~


1.1.0-a.87 <2021-11-8>
-----------------------

New features
~~~~~~~~~~~~

    * Project Management:

        - support load extra project config from `.axio.json` in the same dir with `axio.toml`

    * Package Management:

        - dependencies can be specified by git url directly
        - support `lock_pkgobj` to make sure same pkgobj return for multi ``get_package_object()`` requests
        - component's `toolchain packages` compatible can be specified by manifest's ``toolchains`` item's ``toolchain_packages`` item
        - support use `!#` to apply `git revision check` on any dependencies. eg. use '../path/to/foo!#a5aa55f' to ask check if foo's revision is `a5aa55f`, warning will given if not match.

    * Build System:

        - build function can be ignored via axbuild marker ``@axbuild.mark.ignore``
        - build option schema can be added via axbuild marker ``@axbuild.mark.known_option``
        - simplify `axio-freeze.json` format, friendly to human checking

    * Builders:

        - always ignore ``DEVELOPMENT`` file/directory
        - refactor component builders based on standard ``PackageBuilder``
        - apply schema validation to manifest checking
        - `ComponentBuilder` : append ``buildset`` schema to manifest schema
        - `ComponentBuilder` : ensure BundleBuilder while srcobj is bundle
        - `Platform` support Shared-Library building

    * SCons Build:

        - override original ``Alias`` with ``AxAlias`` , the raw ``Alias`` can be visited by ``SConsAlias``
        - override original ``Default`` with ``AxDefault``, the raw ``Default`` can be visited by ``SConsDefault``
        - new tools: ``AxIsPackage`` ``AxIsFileNode`` ``AxIsDirNode`` ``AxEnsureFileNodes`` ``AxEnsureFsNodes``
        - improve ``AxInstall`` and ``AxInstallAs`` to support copy directories explitly
    
    * Util

        - add ``parse_datastr()`` ``dump_datasr()`` mainly used for translate `match_args` between dict and str
        - apply retry opt. to WebDav Client
        - improve ``match_files()`` , faster and smarter

Bugfixes
~~~~~~~~

    * gcc link command too long will lead to link fail.
    * testsuite cls was bond to not exists module, may cause rel-import fail
    * incorrect temporary file permissions on linux caused test to fail
    * develop/ci test options will be ignored while -tsdist

Incompatible
~~~~~~~~~~~~

    * component object's ``variant`` renamed to ``component_variant``
    * component object's ``get_src_files()`` renamed to ``get_src_build_files()``
    * change ``util.normalize_path()`` change default ``normcase=True`` to ``normcase=False``


1.1.0-a.86 <2021-5-21>
-----------------------

    * fix a bug: `optargs` parsing error while xenv inherits levels are two
    * add new common toolchain ToolchainGccCross
    * fix a bug that the webdav throws `not found` when the path exists in Chinese
    * fix a bug that the datetime object don't has timestamp method under python2 platform
    * fix a bug that axio-cli raise `index out of range` when the result of build is empty
    * fix a bug that fixture ``axiocli`` may lose ``PYTHONPATH`` environment while switch engine
    * unpacker support ``.txz`` ``.bz2``
    * fix a bug that the remote file may not be updated when push the file of same filename
    * fix a bug that matched packages are not optimal when there are extra packages
    * feature encrypt authentication information
    * check administrator privilege on windows
    * feature load the variant modules of repo dynamically
    * feature edition and variant attributes join in engine info of freeze file
    * remove variant attribute when switching engine when the engine version less than 1.1.0-a.86
    * add `app_profile` to identify axio-cli editions and variants
    * update `xenv` to supported inherits xenvs
    * update fixture `isolated_axiohome` to be available in function scope
    * remove the function to upload package to svn in non-variant
    * add variant field in manifest, add filter for variant and add test case
    * add gcc-riscv32 toolchain support

1.1.0-a.85 <2021-4-26>
-----------------------

    * improve the function that upload to SVN
    * make ci check failed message pretty
    * add new ci branch patterns: `fixup-`, `refactor-`, `improve-`
    * improve `ci init` function
    * improve edition function
    * update ci
    * build system back forward compatible : only force setup TARGETS for those builders based on PackageBuilder
    * make fixtures re-usable between axbuild and axtest(pytest)
    * fix a bug that system raise ImportError when switch engine
    * update venv-python37-linux to 1.3709.2
    * fix a bug where a valid package name could not be got if the edition field was not in the manifest
    * ignore `-tfreeze` when switch engine

1.1.0-a.84 <2021-3-23>
-----------------------
    
    * update the version of packages in Rstdocbuilder: tool-miktex@^1.2096300.5, rstdoc-template-zlg^1.2.19
    * the svn client increases support for the linux system
    * add new build option `pydlibs` , used to compile python package to single pyd file
    * fix downloader: make sure `dest_dir` exists before downloading
    * remove deprecated page builder and manager
    * download pre-stage build results as testees in CI environment
    * fixup symlink support under python2 in windows
    * fix a bug that axio-cli can't register the package exactly when exist edition field
    * fix a bug that `get_package_indexings` interface can't filter edition field effectively
    * update all built-in builders based on `PackageBuilder`
    * fix a bug that failed to load build options from manifest's `build` section
    * add new action target `dumpresults` used to dump build results
    * update axbuild script to support axio-cli muli-editions building
    * refactor axio-cli build script by refactored `PackageBuilder`
    * fix a bug that file conflict while building more than one doc target
    * add edition field in manifest and add filter for edition
    * add build target ``autopreview`` for HTML Live preview
    * fix a bug that switched axio engine may lost `pysite-axio` setting
    * fix a bug that framework `sdist` requires `platform` option
    * refactor `PackageBuilder` using `axbuild`
    * new build system `axbuild`
    * fix up env tools supporting: `AxAliasTarget` `AxActionTarget`
    * fix up build options: `targets` `extra_targets`
    * update venv to add decorator, networkx

1.1.0-a.83 <2021-3-9>
-----------------------

    * add component independent build function
    * when matching the requirements, need to be compatible with system field equal to `*`
    * fix a bug that use `os.path.samefile` api incorrectly on Windows
    * update venv-python to fix a bug that there are spaces in the path that cause startup failure
    * upload the files to SVN when create a tag
    * fix a bug that the default encoding of json.dumps under python2 is utf-8, which causes decoding errors to be thrown in other places

1.1.0-a.82 <2021-2-26>
-----------------------

    * feature compatible python3 under linux platform
    * register builder testsuite and srcobj testsuite as pytest plugin
    * refactor `util.collect_filess()` to avoid unnecessary file scanning
    * add virtual box tool for built exe and support to build isolated and single exe

1.1.0-a.81 <2021-2-4>
-----------------------

    * fix a bug that raise Exception when switch the engine
    * fix the problem that copy the pysite data files
    * fix the axio-cli of the python 3 version may not work properly

1.1.0-a.80 <2021-1-6>
-----------------------

    * improve testing fixtures and update venv-python27-linux to 1.2718.2
    * add network reconnect function
    * testing: fixture `axiocli` support linux bash
    * support `XTest`, used for inheritable standard tests
    * python3 CI adapting
    * update venv-axio to 1.2.9, update venv-axio-linux to 1.0.6 and update venv-axio-win-py3 to 1.2.5
    * `PMF` : support `try_update`
    * `axio test` : fixup pytest help, accept pytest args from command line translate them to pytest
    * update venv-axio to 1.2.8, update venv-axio-linux to 1.0.5 and update venv-axio-win-py3 to 1.2.4
    * `axio.util`:
        * `util.Sysenv` : supoort use `<ENVNAME>=None` to remove environment variable `<ENVNAME>`
        * new util: `which` `is_executable_file` `split_command_line`
    * support build python package to single-one pyd file
    * add build tool `AxRemoveTargets`
    * ordered settings items
    * add test fixture `axiocli` and `axiocli_ok`
    * strip `axio.pyd` from `cli_axio.exe` and `builder_runner.exe`
    * fix a bug to generate fault the `xxx.toml` when initialize the project
    * apply schema validation to build options
    * xenv: support condition key
    * fix a bug raise unhashable exception for calling `env_patch` in python3
    * update venv-axio to 1.2.7, update venv-axio-linux to 1.0.4 and update venv-axio-win-py3 to 1.2.3
    * `validation` : support specify python `Class` to `type` filed in schema
    * support `xenv` , used for matrix building
    * make pretty CI script generating
    * support using `regex_name` in schema validation
    * add '-j' build option to control parallel build jobs
    * add tool-scons version to scons signature file
    * update venv-axio to 1.2.6, update venv-axio-linux to 1.0.3 and update venv-axio-win-py3 to 1.2.2
    * add the msvc toolchain support for axio-cli
    * fix a bug that if first param of `open` function is integer format will raise exception in `monkey.py`
    * update venv-axio to 1.2.5 and update venv-axio-win-py3 to 1.2.1
    * ready for testing support
    * update venv-axio-linux to 1.0.2 and fix sorted bug for component
    * modify implement of `__hash__` method
    * update venv-axio to 1.2.4 and update venv-axio-linux to 1.0.1 and update venv-axio-win-py3 to 1.2.0
    * fix a bug that the axio-cli repeatedly import module when module is py file
    * update `venv-axio-win-py3` to 1.1.0
    * fix python3 compatibility bugs
    * remove print_function module
    * modify tool-scons version from ^1 to ^2 in python3
    * fix a bug that `__new__` miss the params
    * add `engine_requirements.axio_engine` field to the manifest be used to check engine version and add the warning for compatibility checks
    * set the default encoding of the execute command function to GBK in python3 on Windows
    * modify venv path's target object name from `venv-rstdoc` to `venv-rstdoc-win-py3` in python3
    * fix some bugs in `build_docs` function
    * set `utf-8` encoding to be the default encoding of axio in python3
    * feature compatible python3
    * subst extensions autoreload from dependencies docs
    * optimize for subst extensions: extensions can be added from options["ext_subst"], BuilderX.EXTENSIONS_FOR_SUBST and template
    * fix a building stuck problem that caused the connection network to get the platform's internal index

1.1.0-a.79 <2020-7-18>
-----------------------

    * fix a bug that target path may can not add file extension name when target filename is this example
      `aw_easyarmrt1021_disk-1.0.2-alpha`

1.1.0-a.78 <2020-6-18>
-----------------------
    * update rstdoc builder, only install components specified by option 'components', will not install all components in framework
    * update axmisc: in AxCopyDataFiles(), exec os.path.normcase() before judging `sss` whether in ignore_sources 
    * update rstdoc builder, add support for frameworks
    * fixed bugs in upgrade
    * fixed is not tty bug with Winpty prompt
    * optimize the code to get production index
    * fixed a bug that prompted Error2 and Error5 when installing the package when 7zip did not exist
    * add two method for component: get_api_files() and get_api_example_files().
      Correspondingly, add two manifest options: `api_file_patterns` and `api_example_specs`
    * fixed install_packages bug: Can't find packages that storage in extra_package_dirs

1.1.0-a.77 <2020-6-10>
-----------------------
    * fixed webdav the bug that failed upload the files when filename include chinese chardet,
      cause the remote server only support utf-8 chardet.
    * support matching packages with multiple `system` requirements

1.1.0-a.76 <2020-5-27>
-----------------------

    * update venv-python27 to 1.2718.3
    * fixed webdav the bug that upload file being empty
    * optimize the display of error messages when `webdav` does not have permissions
    * add `LD_LIBRARY_PATH` to `util.__init__.Venv`
    * fix engine-switch bug : `cli_axio.exe` should be `cli_axio.bin` under linux system
    * update venv-python27-linux to 1.2718.0

1.1.0-a.75 <2020-5-26>
-----------------------

    * fixed bugs in `core.component.__new__`. getting `ENV` is none from `env` when user generates the CI scripts

1.1.0-a.74 <2020-5-25>
-----------------------

    * update venv-python27 to 1.2718.1
    * fixed bugs in `ci.ci_run`.cause CI generates the faulty commands when publishing production

1.1.0-a.73 <2020-5-11>
-----------------------

    * fixed bugs in `rm` and `stat` method  of `axio.util.webdav.WebDav` class.cause the remote path must be format
      before formal request is posted
    * update python env
    * replace webdav lib
    * fixed a bug that failed to compress packages in `util.worker.manager` module
    * add solution builder
    * fixed a bug in `axio.util.__init__.py.load_cls` function,cause may cover first imported module.
    * `env.AxPreparePackage` : ignores package requirements while `system` in-compatible
    * move compatible checking methods to `PackageBase`
    * merge `zip` `7z` `tar.gz` supporting to `env.AxZip`
    * ready for linux


1.1.0-a.72 <2020-5-8>
-----------------------

    * support match packages by `distype`
    * add the `AXIO_SRCOBJ_DEPENDENCIES` variable that are used to save component dependencies to `env` in
      `axio.core.platform` and fixed a bug in `axio.util.__init__.py.load_cls` function,cause may cover
      first imported module.
    * commit changelog of product when user register product
    * fixed a bug in `switch_engine` function.cause when a new frozen file is generated using the --freeze command after
      the engine version is updated, it will be degraded according to the engine version in the old frozen file,
      can not to generate the latest frozen file

1.1.0-a.71 <2020-4-17>
-----------------------

    * support `-D<define>` `-V<variable>` from command line
    * update pyd builder toolset
    * `PackageManager` : fixup install and unsintall functions
    * `AxBuilderBase` : support default targets with chinese characters
    * always try to install `pysite-axio` while switch `axio-engine`

1.1.0-a.70 <2020-4-10>
-----------------------

    * `RstdocBuilder` :
        - prevent parallel sphinx-build
        - launch sphinx-build by the same interpreter used by builder, let builder send objects to sphinx easily
    * new common build target `-tbrowse` : open build directory when building completed
    * `env.AxAlias` : support `cmdstr`
    * `PackageBase` : support use `KNOWN_MANIFEST_ITEMS` to specify package knew manifest items
    * remove duplicate `srcobj` information while building or generating CI scripts
    * update `pysite-axio` to `1.2.0`
    * always enable `deflated` for zip compressing

1.1.0-a.69 <2020-3-18>
-----------------------

    * `RstdocBuilder` : automatically translate sub-head line versions  to `.. describe ::` before building
    * `CHANGELOG.rst` : support using sub-head line to describe versions
    * `env.AxWriteFile()` : support `encoding` argument to specify the output file encoding
    * fix `ci.get_current_axioenv` bug: the assertion is raised when user trigger the job of stop stage
    * fix check frozen file bug in `ci_check` function: because the environment key is not checked in the axio frozen
      file,the check may be abnormally skipped
    * the variant of axio engine name change from `axio` to `axio-engine` in making frozen file
    * check The axio frozen file in `ci_check` function
    * refactor `PackageBuilder` to add custom build-steps easier
    * new util: `normalize_dict_lists()`
    * new builder factory `axio.core.builder.BMF` , use `BMF.get_builder(name)` to get builder class quickly
    * `BulderBase`: do not set default datafiles to `CHANGELOG.rst` and `REAMDE.rst`
    * fix `env.AxInstallFiles` bug: ignores may fail while target is not package root
    * fix `env.AxBuildNow` bug: can not calculate build dependencies correctly while last building raised exceptions
    * new util class `Topic` used to parsing Topic stings
    * rstdoc builder: support `htmlhelp` and `chm` target
    * new component variant `combo`
    * new env methods : `AxAddComponents` `AxPreparePackage` `AxGetDefaultTargets` `AxGetAliasTargets`

1.1.0-a.68 <2020-2-13>
------------------------


   * prepend `winpty` automatically while running in MSYS on windows system
   * support ANSI color output for builder runner
   * fixup ARMCC preprocess function
   * support use `Ctrl+C` to abort axio-cli in terminal
   * new util: `load_cls` and `load_cls_inst`

1.1.0-a.67 <2019-12-31>
------------------------

    * refine exception tracing
    * add dts support
    * feature: use `variant` to specify component is `component` or `bundle`
    * feature: do not process components' dependencies while install, do this in build time
    * add `--ignore-deps` for `install` command
    * fix toolchain check being skipped in special case
    * add long paths support in windows

1.1.0-a.66 <2019-11-27>
------------------------

    * do not append platform and framework version spec while doing `sdist`
    * new feature: optionally looking for packages in global storage while the manager's package storage is not the global one
    * add silent command support
    * update venv-python dependency
    * refine build processing
    * fix up freeze function for components building
    * remove *.pyc from venv-axio-cli

    * fix big bug: ci will only keep one package on the same STAGE, the others will be removed from indexing.
    * new env method env.AxAction()
    * auto transfer exception.BuildError to SCons.Errors.StopError
    * dist venv-axio-cli

    * get_libs() changes: return FsNode
    * package manager: use __new__ to hack cache functions
    * always remove `fameworks` from framework manifest
    * update default building : only build the builds returned by axbuilders
    * update env.AxWriteFile() : support use env.Literal to escape `$` char
    * update component builder
    * support BuilderX
    * fix axiowinhooks : support armcc cmd line
    * update platform env processing
    * update component dist function
    * Component Application Framework Board Platform 支持 sdist
    * [BuilderBase]：
        * 将 build 流程从 class 级别转移至 instance 级别 2019-7-17
    * env.AxTool 支持同时加载多个 tools
    * framework 增加属性 pypath buildtools
    * 分离与 aworks framework 有关的工具
    * 重构 platform framework board component application 继承关系
    * toolchain 抽象为独立的包类型
    * 修复默认使用 envname 作为 manifest name 的BUG
    * 修复 datafiles 不能强制添加“被自动忽略文件”的问题
    * [axio] 配置段中符合 extra_*_dir 、 extra_*_drs 模式的选项都设置为已知选项
    * rstdoc builder 默认使用 envname 作为 manifest name ，便于向后兼容 ~1.0.0
    * 默认创建 review 的 stop job ，当删除分支时 可自动移除注册的包
    * fix util.simple_match() bug
    * 默认不再创建 review 、 staging  的 stop job
    * 支持 `ci.manual_jobs` option
    * 更新 axio init 命令
    * PackageBuilder 添加默认 datafiles
    * 升级 datafiles 描述，支持多个 source 和 filter ，自动过滤不必要的文件
    * 修复问题自动过滤掉 `.` 开头的文件
    * 修复 package builder sdist BUG
    * 修复 online-doc bug
    * 将 base url 使用 BUILD_SLUG  改为 BUILD_REF
    * 修复 category BUG 2019.4.25
    * 修复 rstdoc builder ci init 问题 2019.4.25
    * 添加附件功能
    * manifest 不再依赖不必要的 source
    * 适配新的AXPI接口
    * 增加 freeze 功能
    * 下载包默认 silent
    * update ci_check
    * 修复CI环境下 unicode 问题
    * 将 `requests` 包从 `axpi` 中移除
    * 增加 setting `username` 和 `password`
    * `axio ci init` 命令增加选项 `--no-engine-freeze` `--axio-cmd`
    * 将 pysite-axio 从 axio-engine 中拆分出来
    * CI 绑定 axio-engine 版本
    * 更新 scons 依赖为 `^1`
    * 更新 CI 策略：包路径加上 build_ref_flug ，便于利用 gitlab 的动态环境
    * 修复问题：安装新包后，get_installed() 和 get_package_object() cache 清空，导致不能使用新安装的包
    * 新增 `AxZIP` build tool， `deflated` 的选项可减少压缩包体积
    * 更新 `register` 接口
    * 修复 `upgrade` 命令
    * 删除不必要的命令
    * 修复 install uninstall download latest 命令
    * 重构 register unregister publish
    * 将 axbuilder/main.py 移至 AxBuilder.build()
    * 将 `package_manager.axbuilder` 等包管理器与主程序 axio 一同打包发布
    * 将 `axbuilder.package` 等构建器与主程序 axio 一同打包发布
    * 新增 program 构建期
    * 若干 bug 修复和小功能添加


1.0.41-a.14 <2018-1-23>
------------------------

    * :feature:`7083`
    * 将 custom builder 独立出来
    * `build` 命令添加 `--with-vdrv` 选项
    * `axio.toml` 添加选项 `axio.build_with_vdrv`
    * 修复 package unregister 总是返回成功的问题
    * `axio.toml` 选项 `axio.default_env` 会传递到 `include` 中的 `project`
    * `axio.toml` 添加选项 `axio.extra_<package_type>_dir` ，支持添加额外的包路径
    * `package manifest` 成员 `builder` 和 `packer` 显示完整包名
    * 增加 `package status` 用于区分 `stable` `alpha` `beta` 等包状态

1.0.40 <2017-12-7>
------------------------

    * :feature:`6835`
    * 增加对非 semantic-version 版本号支持
    * 修复 axio home unicode 编码问题
    * 增加 pkg-resource 依赖包
    * 修复Windows中文路径编码问题

1.0.30 <2017-11-18>
------------------------

    * 检查必须的的 build options
    * 生成python包时，将 axio 的 semver 转为 pepver
    * 更新 setup 文件：去除 syspath 的打印信息
    * 添加CI命令
    * 增加 YAML 模块

1.0.28 <2017-11-14>
------------------------

    * PackageRepoFactory类增加通过名字获取repo实例的方法
    * PackageRepo类增加计算package根路径的接口
    * install 提示信息加上包类型
    * 默认不再下载repolist，否则断网时将奇慢无比
    * update、list 命令中显示 package_mananger
    * 修复默认axbuilder版本获取失败问题
    * 在 validate_options 步骤中添加 env 参数
    * 修复download CACHE 文件名错误
    * 合并仓库迭代器类
    * 分离 axio 的python环境
    * 移除axbuilder、package模块中重复的类
    * 支持 install、uninstall、update命令
    * 修复不能正确识别版本号为两位数的问题
    * 基本支持 RSTDOC build
    * 支持完整的Semantic Version
    * 修复问题：当版本号中带'-'时会构建失败

1.0.0 <2017-9-10>
------------------------

    * first implement

