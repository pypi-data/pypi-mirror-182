# -*- coding:utf-8 -*-
# Copyright (c) 2001-present Guangzhou ZHIYUAN Electronics Co., Ltd..
# All rights reserved.

from os.path import basename, dirname
from axio.exception import AxioException, ScriptEntryNotFound
from SCons import Errors

Import('env', 'script_path', 'script_entry')

env.Tool(basename(script_path).split('.', 1)[0], toolpath=[dirname(script_path), ])
try:
    try:
        entry = getattr(env, script_entry)
    except AttributeError:
        raise ScriptEntryNotFound(script_entry, script_path)
    result = entry()
except AxioException as e:
    raise Errors.StopError(e)
except WindowsError as e:
    raise Errors.StopError(e)

result = [] if not result else result
Return(result)




