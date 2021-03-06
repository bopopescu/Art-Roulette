# -*- coding: utf-8 -*- #
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

"""`gcloud iot registries create` command."""

from __future__ import absolute_import
from __future__ import unicode_literals

from googlecloudsdk.api_lib.cloudiot import registries
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.iot import flags
from googlecloudsdk.command_lib.iot import resource_args
from googlecloudsdk.command_lib.iot import util
from googlecloudsdk.core import log


def _Run(args, supports_deprecated_event_config_flags=False):
  """Creates a new Cloud IoT Device Registry."""
  client = registries.RegistriesClient()

  registry_ref = args.CONCEPTS.registry.Parse()
  location_ref = registry_ref.Parent()

  mqtt_state = util.ParseEnableMqttConfig(args.enable_mqtt_config,
                                          client=client)
  http_state = util.ParseEnableHttpConfig(args.enable_http_config,
                                          client=client)

  event_pubsub_topic = None
  if supports_deprecated_event_config_flags:
    event_pubsub_topic = args.event_pubsub_topic
  event_notification_configs = util.ParseEventNotificationConfig(
      args.event_notification_configs, event_pubsub_topic)

  state_pubsub_topic_ref = util.ParsePubsubTopic(args.state_pubsub_topic)
  credentials = []
  if args.public_key_path:
    credentials.append(util.ParseRegistryCredential(args.public_key_path))

  response = client.Create(
      location_ref, registry_ref.registriesId,
      credentials=credentials,
      event_notification_configs=event_notification_configs,
      state_pubsub_topic=state_pubsub_topic_ref,
      mqtt_enabled_state=mqtt_state,
      http_enabled_state=http_state)
  log.CreatedResource(registry_ref.registriesId, 'registry')
  return response


@base.ReleaseTracks(base.ReleaseTrack.GA)
class Create(base.CreateCommand):
  """Create a new device registry."""

  @staticmethod
  def Args(parser):
    resource_args.AddRegistryResourceArg(parser, 'to create')
    flags.AddDeviceRegistrySettingsFlagsToParser(parser,
                                                 include_deprecated=False)
    flags.AddDeviceRegistryCredentialFlagsToParser(
        parser, credentials_surface=False)

  def Run(self, args):
    return _Run(args)


@base.ReleaseTracks(base.ReleaseTrack.BETA)
class CreateBeta(base.CreateCommand):
  """Create a new device registry."""

  @staticmethod
  def Args(parser):
    resource_args.AddRegistryResourceArg(parser, 'to create')
    flags.AddDeviceRegistrySettingsFlagsToParser(parser)
    flags.AddDeviceRegistryCredentialFlagsToParser(
        parser, credentials_surface=False)

  def Run(self, args):
    return _Run(args, supports_deprecated_event_config_flags=True)
