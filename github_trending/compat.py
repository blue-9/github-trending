# -*- coding: utf-8 -*-

# Copyright 2015 Donne Martin. All Rights Reserved.
# Modifications copyright 2018 Yuya Chiba.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import urllib
try:
    # Python 3
    import configparser
    from urllib.request import urlretrieve
except ImportError:
    import ConfigParser as configparser
    from urllib import urlretrieve
