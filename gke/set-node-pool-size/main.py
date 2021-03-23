from pprint import pprint
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import os

# https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/setSize

credentials = GoogleCredentials.get_application_default()
service = discovery.build("container", "v1", credentials=credentials)
project_id = os.environ.get("GCP_PROJECT")


def set_node_pool_size(request):
    location = "cluster-location" # TODO
    cluster_name = "cluster-name" # TODO
    node_pool = "node-pool-name" # TODO

    # Specified in the format 'projects/*/locations/*/clusters/*/nodePools/*'.
    name = f"projects/{project_id}/locations/{location}/clusters/{cluster_name}/nodePools/{node_pool}"

    updated_body = {"nodeCount": X} # TODO: Replace X with the desired amount(int) of instances

    request = (
        service.projects()
        .locations()
        .clusters()
        .nodePools()
        .setSize(name=name, body=updated_body)
    )

    response = request.execute()

    pprint(response)
