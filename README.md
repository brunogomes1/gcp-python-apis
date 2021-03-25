# How to use/interact with it

The bucket and eventual files can be created with Terraform, files can also be uploaded using gsutil.

Structure : <bucket_name> / <repo_name> / <api_folder> / <api_name> / <main.py | requirements.txt>


## Using gsutil command line to upload the files:

Ensure the above steps are already completed

1 - Go to the desired path where the files main.py | requirements.txt are;
2 - Select the 2 files that you want and zip them into a new archive. Note: Do not zip the folder where the 2 files are. Cloud Function is not able to read folders. The zip archive must have 2 files inside it, main.py | requirements.txt. It cant be a zip archive with a folder inside it with 2 files inside this folder.
3 - Open the terminal;
4 - Run the following commands:

```
gcloud config set project <project_name>

gsutil cp < path on your computer with the zip archive(.zip) > gs://<bucket_name>/folder_if_you__want/<other_folder_if_you__want>/<api_name>/

```

5 - Deploy the cloud function via Terraform pointing to the file on the bucket.

# Terraform

## Terraform module usage:

module "srlab-oms-function-test"{
    source                        = "./modules/cloud-functions"
    project                       = var.project
    cloud_function_name           = "function-test"
    function_runtime              = "python37"
    description                   = "Test function to interact with GKE node pool"
    available_memory_mb           = 256
    trigger_http                  = true
    entry_point                   = "def_function_name"
    ingress_settings              = "ALLOW_ALL"
    svc_acc_prefix                = "svc-terraform"
    source_archive_bucket         = "terraform-test"
    source_archive_object         = "folder_inside_bucket_1/folder_inside_folder/Archive.zip"

    env_variables                 = {

      CLUSTER_LOCATION            = ""
      CLUSTER_NAME                = ""
      NODE_POOL_NAME              = ""
      DESIRED_NODE_COUNT          = ""

  }
}
