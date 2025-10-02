output "s3_bucket" {
  value = aws_s3_bucket.raw_files.bucket
}

output "dynamodb_table" {
  value = aws_dynamodb_table.processed.name
}

output "lambda_function" {
  value = aws_lambda_function.processor.arn
}
