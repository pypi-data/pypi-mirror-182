# -*- coding:utf-8 -*-
# Copyright (c) 2001-present Guangzhou ZHIYUAN Electronics Co., Ltd..
# All rights reserved.

import os
from axio.core.manager import PackageManagerFactory

PackageManagerFactory.new_pm('axbuilder').get_package_object(os.environ['AXIO_AXBUILDER_MANIFEST']).build_processing()
