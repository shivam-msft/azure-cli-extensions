# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals
from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from ._client_factory import cf_peer_asns
    peering_peer_asns = CliCommandType(
        operations_tmpl='azext_peering.vendored_sdks.peering.operations.peer_asns_operations#PeerAsnsOperations.{}',
        client_factory=cf_peer_asns)
    with self.command_group('peering asn', peering_peer_asns, client_factory=cf_peer_asns) as g:
        g.custom_command('create', 'create_peering_asn')
        g.generic_update_command('update', custom_func_name='update_peering_asn')
        g.command('delete', 'delete')
        g.custom_command('list', 'list_peering_asn')
        g.show_command('show', 'get')

    from ._client_factory import cf_peerings
    peering_peerings = CliCommandType(
        operations_tmpl='azext_peering.vendored_sdks.peering.operations.peerings_operations#PeeringsOperations.{}',
        client_factory=cf_peerings)
    with self.command_group('peering', peering_peerings, client_factory=cf_peerings) as g:
        g.custom_command('create', 'create_peering')
        g.generic_update_command('update', custom_func_name='update_peering')
        g.command('delete', 'delete')
        g.custom_command('list', 'list_peering')
        g.show_command('show', 'get')

    from ._client_factory import cf_prefixes
    peering_prefixes = CliCommandType(
        operations_tmpl='azext_peering.vendored_sdks.peering.operations.prefixes_operations#PrefixesOperations.{}',
        client_factory=cf_prefixes)
    with self.command_group('peering service prefix', peering_prefixes, client_factory=cf_prefixes) as g:
        g.custom_command('create', 'create_peering_service_prefix')
        g.generic_update_command('update', custom_func_name='update_peering_service_prefix')
        g.command('delete', 'delete')
        g.custom_command('list', 'list_peering_service_prefix')
        g.show_command('show', 'get')

    from ._client_factory import cf_peering_services
    peering_peering_services = CliCommandType(
        operations_tmpl='azext_peering.vendored_sdks.peering.operations.peering_services_operations#PeeringServicesOperations.{}',
        client_factory=cf_peering_services)
    with self.command_group('peering service', peering_peering_services, client_factory=cf_peering_services) as g:
        g.custom_command('create', 'create_peering_service')
        g.generic_update_command('update', custom_func_name='update_peering_service')
        g.command('delete', 'delete')
        g.custom_command('list', 'list_peering_service')
        g.show_command('show', 'get')