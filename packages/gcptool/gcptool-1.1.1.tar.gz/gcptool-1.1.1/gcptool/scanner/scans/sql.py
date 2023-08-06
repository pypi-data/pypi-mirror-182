from typing import Dict, List, Optional

from gcptool.inventory.sql import instances, users
from gcptool.scanner.context import Context
from gcptool.scanner.finding import Finding, Severity
from gcptool.scanner.scan import Scan, ScanMetadata, scan


@scan
class SQLInventory(Scan):
    @staticmethod
    def meta() -> ScanMetadata:
        return ScanMetadata(
            "sql",
            "inventory",
            "Inventory of Cloud SQL resources",
            Severity.INFO,
            ["roles/iam.securityReviewer"],
        )

    def run(self, context: Context) -> Optional[Finding]:

        for project in context.projects:
            servers = instances.all(project.id, context.cache)

            for server in servers:
                u = users.all(project.id, server.id, context.cache)


@scan
class TLSEnforcement(Scan):
    """
    Checks that all Cloud SQL instances that are available on the public internet require SSL.
    """

    @staticmethod
    def meta():
        return ScanMetadata(
            "sql",
            "tls",
            "Cloud SQL instances do not require TLS",
            Severity.LOW,
            ["roles/iam.securityReviewer"],
        )

    def run(self, context: Context) -> Optional[Finding]:
        vulnerable_by_project: Dict[str, List[instances.Instance]] = {}

        for project in context.projects:

            p = instances.all(project.id, context.cache)

            open_instances: List[instances.DatabaseInstance] = []

            for instance in p:
                has_public_ip = False
                for address in instance.ip_addresses:
                    if address.type == instances.SQLIPAddressType.PRIMARY:
                        has_public_ip = True

                # We need to check if this is actually available over the internet.
                # If there's an IP, but no authorized networks, then this instance isn't actually public.
                # (Except for throug the Cloud SQL proxy, which always uses SSL.)
                has_authorized_networks = len(instance.ip_configuration.authorized_networks) > 0

                requires_ssl = instance.ip_configuration.require_ssl

                if has_public_ip and has_authorized_networks and not requires_ssl:
                    open_instances.append(instance)

            if len(open_instances) > 0:
                vulnerable_by_project[project.id] = open_instances

        if len(vulnerable_by_project):
            return self.finding(vulnerable_projects=vulnerable_by_project)

        return None


@scan
class RootLoginFromAnyHost(Scan):
    @staticmethod
    def meta() -> ScanMetadata:
        return ScanMetadata(
            "sql",
            "root_login",
            "Cloud SQL instances allow root login from any host",
            Severity.LOW,
            ["roles/iam.securityReviewer"],
        )

    def run(self, context: Context) -> Optional[Finding]:

        found = []

        for project in context.projects:

            p = instances.all(project.id, context.cache)

            for instance in p:

                if not instance.database_version.value.startswith("MYSQL"):
                    continue

                u = users.all(project.id, instance.id, context.cache)

                for user in u:
                    if user.name != "root":
                        continue

                    if user.host in {"%", "0.0.0.0", "/0"}:
                        found.append(instance)

        if len(found):
            return self.finding(instances=found)
