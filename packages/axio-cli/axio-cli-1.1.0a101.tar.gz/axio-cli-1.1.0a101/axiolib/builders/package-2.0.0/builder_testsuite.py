# -*- coding:utf-8 -*-  
# Copyright (c) 2001-present Guangzhou ZHIYUAN Electronics Co., Ltd..
# All rights reserved.

import pytest

from axio import util, exception
from axio.core.manager import PMF

class BuilderTestsuiteX(object):
    pass
    # @pytest.hookimpl(hookwrapper=True)
    # def pytest_pycollect_makeitem(self, collector, name, obj):
    #     outcome = yield
    #     res = outcome.get_result()
    #     pass


@pytest.mark.usefixtures('inject_testees')
class XTestPackage(object):

    def test_manifest(self, srcobj):
        assert srcobj.name
        assert srcobj.version


@pytest.mark.usefixtures('inject_testees')
@pytest.mark.isolated_axiohome(export_packages=['tool*', 'venv*'])
class XTestExample(object):

    # use individual axiocli cmd process
    @pytest.fixture(scope="module")
    def _axiocli(self, _axiocli_cls):
        with _axiocli_cls() as axiocli:
            yield axiocli

    @pytest.fixture(scope='function')
    def axiohome(self, request, testees):

        # decide isolated axio home kwargs by testees :  ignore all packages same name with testees
        ignores = ['{}.{}'.format(x.category, x.name) for x in testees]
        request.node.add_marker(pytest.mark.isolated_axiohome(ignore_packages=ignores))

        return request.getfixturevalue('axiohome')

    def test_same_packages_should_have_been_ignored(self, builder, testees):
        if not builder.dist_targets:
            pytest.skip('only do this test when dist')

        # only testee can be found with the same category and name
        for testee in testees:
            found = [x for x in PMF.get_installed(testee.category, as_objects=True) if x.name == testee.name]
            assert len(found) == 1, 'Found {}'.format(found)
            assert found[0].get_dir() == testee.get_dir()

    def test_example_build(self, example, axiocli_ok):
        with util.cd(example):
            axiocli_ok(['build', '-i', '-v', '-tclean'])
            result = axiocli_ok(['build', '-i', '-v'])

            # todo: better way to report log
            for line in result.lines:
                print(line)

