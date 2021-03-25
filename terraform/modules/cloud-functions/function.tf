resource "google_cloudfunctions_function" "http_function" {
  name                          = var.cloud_function_name
  project                       = var.project
  runtime                       = var.function_runtime
  description                   = var.description
  available_memory_mb           = var.available_memory_mb
  trigger_http                  = var.trigger_http
  entry_point                   = var.entry_point
  ingress_settings              = var.ingress_settings
  labels                        = var.labels
  service_account_email         = "${var.svc_acc_prefix}@${var.project}.iam.gserviceaccount.com"
  source_archive_bucket         = var.source_archive_bucket
  source_archive_object         = var.source_archive_object
  environment_variables         = var.env_variables


}

output "url"{
  value = google_cloudfunctions_function.http_function.https_trigger_url
}
