from pprint import pprint
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import os

credentials = GoogleCredentials.get_application_default()
service = discovery.build("sqladmin", "v1beta4", credentials=credentials)
project_id = os.environ.get("GCP_PROJECT")

def cloudsql_on(request):
    activation_policy = "NEVER"
    instance_name = "instance-name" # TODO

    dbinstancebody = {"settings": {"activationPolicy": activation_policy}}

    request = service.instances().patch(
        project=project_id, instance=instance_name, body=dbinstancebody
    )
    response = request.execute()

    pprint(response)
