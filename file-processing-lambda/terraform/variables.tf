variable "aws_region" {
  default = "us-east-1"
}

variable "s3_bucket_name" {
  description = "S3 bucket name (must be globally unique)"
  type        = string
}

variable "dynamodb_table" {
  default = "ProcessedData"
}

variable "lambda_zip_path" {
  description = "Path to lambda zip package"
  type        = string
}

variable "lambda_function_name" {
  default = "rt-file-processor"
}
