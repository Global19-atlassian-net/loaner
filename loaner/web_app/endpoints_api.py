# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Endpoints API main entrance."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import endpoints

from loaner.web_app.backend.api import bootstrap_api  # pylint: disable=unused-import
from loaner.web_app.backend.api import config_api  # pylint: disable=unused-import
from loaner.web_app.backend.api import datastore_api  # pylint: disable=unused-import
from loaner.web_app.backend.api import device_api  # pylint: disable=unused-import
from loaner.web_app.backend.api import root_api
from loaner.web_app.backend.api import search_api  # pylint: disable=unused-import
from loaner.web_app.backend.api import shelf_api  # pylint: disable=unused-import
from loaner.web_app.backend.api import survey_api  # pylint: disable=unused-import
from loaner.web_app.backend.api import tag_api  # pylint: disable=unused-import
from loaner.web_app.backend.api import template_api  # pylint: disable=unused-import
from loaner.web_app.backend.api import user_api  # pylint: disable=unused-import

ENDPOINTS_API = endpoints.api_server([root_api.ROOT_API])
