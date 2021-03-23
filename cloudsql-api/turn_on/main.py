from pprint import pprint
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()
service = discovery.build("sqladmin", "v1beta4", credentials=credentials)

def cloudsql_on(request):
    project = "your-project-id" # TODO
    instance_name = "instance-name" # TODO

    dbinstancebody = {"settings": {"activationPolicy": "ALWAYS"}}

    request = service.instances().patch(
        project=project, instance=instance_name, body=dbinstancebody
    )
    response = request.execute()

    pprint(response)
