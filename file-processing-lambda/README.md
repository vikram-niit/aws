# Real-Time File Processing Pipeline (S3 → Lambda → DynamoDB)

## Overview

This project implements a serverless pipeline that automatically processes files uploaded to Amazon S3. When a file (CSV/JSON) is uploaded, an AWS Lambda function is triggered to parse, clean, and store records in DynamoDB.

## Architecture

- User/System uploads files to S3
- S3 triggers Lambda on `ObjectCreated`
- Lambda reads & processes file
- Processed records stored in DynamoDB
- CloudWatch logs hold function logs; SNS optional for alerts

## Files

- `lambda/lambda_function.py` — lambda handler (Python)
- `terraform/` — Terraform files to create infra
- `cdk/` — CDK TypeScript stack (optional)
- `README.md` — this file

## Deployment (quick)

1. Create S3 bucket
2. Create DynamoDB `ProcessedData` table
3. Create IAM role for Lambda
4. Package function:

   ```bash
   cd lambda
   zip -r ../lambda_function.zip .
5. Create Lambda (or use Terraform/CDK)

6. Configure S3 notification to invoke Lambda

## Testing
Upload sample_file.csv to the S3 bucket:

aws s3 cp sample_file.csv s3://<bucket-name>/uploads/sample_file.csv
Check CloudWatch logs for rt-file-processor.

## Terraform usage
### Infrastructure as Code

Use the terraform/ folder for Terraform examples, or the cdk/ folder for AWS CDK (TypeScript) to provision resources.

Build the Lambda zip:

```bash
cd lambda && zip -r ../lambda_function.zip . && cd ..
```

Then, run the following Terraform commands:

```bash
terraform init
terraform apply -var "s3_bucket_name=my-unique-bucket-123" -var "lambda_zip_path=./lambda_function.zip"
```

## Enhancements
- Use SQS for large/batch processing
- Add Step Functions for long-running transforms
- Add RDS for relational storage
- Add validation, schema checks, and observability dashboards



