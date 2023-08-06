from googleapiclient.discovery import build

from gcptool.creds import credentials

# The actual API name for Kubernetes Engine is just "container" for some reason
client = build("container", "v1beta1", credentials=credentials)

# pylint: disable=no-member
clusters = client.projects().locations().clusters()

# pylint: disable=no-member
node_pools = clusters.nodePools()
