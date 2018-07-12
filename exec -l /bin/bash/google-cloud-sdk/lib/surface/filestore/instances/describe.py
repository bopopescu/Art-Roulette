# Copyright 2017 Google Inc. All Rights Reserved.
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
"""Command to show metadata for a Cloud Filestore instance."""

from __future__ import absolute_import
from __future__ import unicode_literals
from googlecloudsdk.api_lib.filestore import filestore_client
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.filestore import flags
from googlecloudsdk.command_lib.util.concepts import concept_parsers


class Describe(base.DescribeCommand):
  """Show metadata for a Cloud Filestore instance.

  ## EXAMPLE

  The following command shows the metadata for the Cloud Filestore instance
  named NAME in us-central1-c.

    $ {command} NAME --location=us-central1-c
  """

  @staticmethod
  def Args(parser):
    concept_parsers.ConceptParser([flags.GetInstancePresentationSpec(
        'The instance to describe.')]).AddToParser(parser)

  def Run(self, args):
    """Run the describe command."""
    instance_ref = args.CONCEPTS.instance.Parse()
    return filestore_client.FilestoreClient().GetInstance(instance_ref)
