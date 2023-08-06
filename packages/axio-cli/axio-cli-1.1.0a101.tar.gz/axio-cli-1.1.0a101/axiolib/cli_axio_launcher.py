# -*- coding:utf-8 -*-
# Copyright (c) 2001-present Guangzhou ZHIYUAN Electronics Co., Ltd..
# All rights reserved.

import sys
import os
import platform
import subprocess
import glob
import re


_ansi_re = re.compile('\033\[(((?:\d|;)*)|(\?(?:\d|;)*))([a-zA-Z])')


def strip_ansi(value):
    PY2 = sys.version[0] == '2'
    value = value if PY2 else str(value, sys.getdefaultencoding())
    return _ansi_re.sub('', value).replace('\r\n', '')


def copy_pythonpath_to_osenv():
    _PYTHONPATH = []
    if "PYTHONPATH" in os.environ:
        _PYTHONPATH = os.environ.get("PYTHONPATH").split(os.pathsep)
    for p in sys.path:
        conditions = [p not in _PYTHONPATH]
        if all(conditions):
            _PYTHONPATH.append(p)
    os.environ['PYTHONPATH'] = os.pathsep.join(_PYTHONPATH)


def get_source_dir():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS

    curpath = os.path.abspath(__file__)
    if not os.path.isfile(curpath):
        for p in sys.path:
            if os.path.isfile(os.path.join(p, __file__)):
                curpath = os.path.join(p, __file__)
                break
    return os.path.dirname(curpath)


def call_cmd(*args):
    result = dict(out=None, err=None, returncode=None)
    p = subprocess.Popen(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, result['err'] = p.communicate()
    result['returncode'] = p.returncode
    result['out'] = strip_ansi(out)
    return result


def parse_cli_verstr(s):
    ret = re.findall('([^,]+),\s*(([a-zA-Z0-9-_]*)(\(([a-zA-Z0-9-_]*)\))?,\s*)?version\s+(\S*)', s.strip())
    if ret:
        return ret[0][5], ret[0][2], ret[0][4]


def get_current_version():
    result = call_cmd(['axio', '--version'])
    if result['returncode'] == 0:
        return parse_cli_verstr(result['out'].strip())


def get_latest_version(version, stage, status):
    cmds = ['axio', 'package', 'latest', 'axio-cli']
    if version:
        cmds[-1] = 'axio-cli@' + version
    if stage:
        cmds.append('-T' + stage)
    if status:
        cmds.append('-S' + status)
    result = call_cmd(cmds)
    if result['returncode'] == 0:
        return result['out'].strip().split("version", 1)[1].strip()
    else:
        return None


def download_axio(version, stage, status):
    cmds = ['axio', 'package', 'install', 'axio-cli@' + version, ]
    if stage:
        cmds.append('-T' + stage)
    if status:
        cmds.append('-S' + status)
    result = call_cmd(cmds)
    if result['returncode'] == 0:
        return result['out'].strip().split("installed at", 1)[1].strip()
    else:
        return None


def delete_axio(version):
    result = call_cmd(['axio', 'package', 'uninstall', 'axio-cli@' + version, ])
    return result['returncode']


class cd(object):

    def __init__(self, new_path):
        self.new_path = new_path
        self.prev_path = os.getcwd()

    def __enter__(self):
        os.chdir(self.new_path)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.prev_path)


def _process_args(args):
    if not args:
        return []
    _args = []
    for arg in args:
        if '=' in arg:
            _args.extend(arg.split('='))
        else:
            _args.append(arg)
    return _args


def _append_ev(req_version, edition=None, variant=None):
    if '(' not in req_version:
        mats = []
        if edition and 'edition' not in req_version:
            mats.append("edition='{}'".format(edition))
        if variant and 'variant' not in req_version:
            mats.append("variant='{}'".format(variant))
        if mats:
            req_version += '({})'.format(','.join(mats))
    return req_version


def upgrade(args):
    req_version = stage = status = force = only_check = None
    args = _process_args(args)

    skip = False
    for i, arg in enumerate(args):
        if skip:
            skip = False
            continue

        if arg in ['--stage', '--status']:
            try:
                val = args[i + 1]
            except IndexError:
                print('option `%s` missing value' % arg)
            if arg is '--stage':
                stage = val
            elif arg is '--status':
                status = val
            else:
                print('unknown option %s' % arg)
                return 2
            skip = True

        elif arg.startswith('-T'):
            stage = arg.split('-T', 1)[1]
        elif arg.startswith('-S'):
            status = arg.split('-S', 1)[1]
        elif arg == '--force':
            force = True
        elif arg in ['-c', '--only-check']:
            only_check = True
        elif arg[0].isdigit() or arg[0] in ['~', '^', '>', '<', '=', '!']:
            if req_version:
                print('bad argument `%s`' % arg)
                return 2
            req_version = arg
        else:
            print('unknown argument `%s`' % arg)
            return 2

    cur_version, edition, variant = get_current_version()
    if req_version is None:
        req_version = cur_version
    req_version = _append_ev(req_version, edition, variant)

    latest = get_latest_version(req_version, stage, status)
    if not latest:
        print("Can't get the latest axio-cli version, Please check your net and permission!")
        return 2

    if cur_version == latest and not force:
        print("You're up-to-date!\naxio-cli %s is currently the newest version available." % _append_ev(cur_version, edition, variant))
    elif only_check:
        print("%s -> %s %s" % (cur_version, latest, _append_ev('', edition, variant)))

    else:
        print("Please wait while upgrading axio-cli (%s -> %s), may need some time..." % (cur_version, latest))
        sys.stdout.flush()

        # append edition and variant
        latest = _append_ev(latest, edition, variant)

        # force remove old one
        if force:
            delete_axio(latest)

        # download axio
        pkgdir = download_axio(latest, stage, status)
        if not pkgdir:
            print("Downloading axio-cli@{} failed, please check your permission".format(latest))
            return 2

        with cd(pkgdir):
            pkg = glob.glob('*.tar.gz')[0]

            call_cmd(['pip', 'uninstall', 'axio-cli', '-y'])

            cmd = ['pip', 'install', pkg, '-I']
            r = call_cmd(cmd)
            # try pip with disabled cache
            if r['returncode'] != 0:
                cmd.insert(1, "--no-cache-dir")
                r = call_cmd(cmd)

            if r['returncode'] != 0:
                print("Install axio-cli FAILED! [%s]" % r['returncode'])
                return r['returncode']
        # remove cache
        delete_axio(latest)

        # print actual version
        actual_version, edition, variant = get_current_version()
        print("axio-cli has been successfully upgraded to %s" % actual_version)
        print("Release notes: ")
        print("http://axpi/production/changelog/?production_id=15")
    return 0


def main():
    # upgrade processing
    # sys.argv.extend(['upgrade', '-Treview', '-Sany'])
    if len(sys.argv) >= 2 and sys.argv[1] == 'upgrade' and '--help' not in sys.argv and '-h' not in sys.argv:
        args = sys.argv[2:] if len(sys.argv) > 2 else []
        return upgrade(args)

    os.environ['PYTHONEXEPATH'] = os.path.normpath(sys.executable)

    pysite_axio = os.path.join(get_source_dir(), 'pysite-axio')
    pysite_axio = pysite_axio if os.path.exists(pysite_axio) else os.getenv('AXIOPYSITEDIR', None)
    if pysite_axio:
        os.environ['AXIOPYSITEDIR'] = pysite_axio
        sys.path.insert(0, pysite_axio)

    copy_pythonpath_to_osenv()

    cmd = []

    # prepend winpty while running in msys on windows
    if platform.system().lower() == 'windows' and os.getenv('MSYSTEM') and call_cmd(['where', 'winpty'])[
        'returncode'] == 0:
        cmd += ['winpty', '-Xallow-non-tty']

    launcher_name = "cli_axio.exe" if platform.system().lower() == 'windows' else "cli_axio.bin"
    cmd += [os.path.join(get_source_dir(), 'bin', launcher_name)]
    cmd += sys.argv[1:]
    try:
        return subprocess.call(cmd)
    except:
        return 1


if __name__ == '__main__':
    sys.exit(main())
