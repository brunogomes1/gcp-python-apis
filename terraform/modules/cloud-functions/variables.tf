variable "project" {
  description = "The project ID"
  type        = string
}

variable "cloud_function_name" {
  description = ""
  type        = string
}

variable "function_runtime" {
  description = ""
  type        = string
}

variable "description" {
  type        = string
}

variable "available_memory_mb" {
  description = ""
  type        = number
}

variable "trigger_http" {
  description = ""
  type        = bool
}

variable "labels" {
  type        = map(string)
  description = "A map of labels to assign to the Cloud Function"
  default     = {}
}

variable "env_variables" {
  type        = map(string)
  description = "A map of variables to assign to the Cloud Function"
  default     = {}
}

variable "svc_acc_prefix" {
  type        = string
  description = "Usually the name that has been chosen for this service account"
}

variable "entry_point" {
  description = "The python function(def) name"
  type        = string
}

variable "ingress_settings" {
  description = ""
  type        = string
}

variable "source_archive_bucket" {
  description = ""
  type        = string
}

variable "source_archive_object" {
  description = "with this format: folder-inside-bucket/other-folder/other-folder-if-you-have/filename.zip"
  type        = string
}
