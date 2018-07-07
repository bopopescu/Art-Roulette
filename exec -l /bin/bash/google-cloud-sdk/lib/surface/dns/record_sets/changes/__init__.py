# -*- coding: utf-8 -*- #
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""gcloud dns record-sets changes command group."""

from __future__ import absolute_import
from __future__ import unicode_literals
from googlecloudsdk.calliope import base


class Changes(base.Group):
  """View details about changes to your Cloud DNS record-sets.

  View details about changes to your Cloud DNS record-sets.

  ## EXAMPLES

  To view the details of a particular change, run:

    $ {command} describe CHANGE_ID --zone MANAGED_ZONE

  To view the list of all changes, run:

    $ {command} list --zone MANAGED_ZONE

  """
  pass
