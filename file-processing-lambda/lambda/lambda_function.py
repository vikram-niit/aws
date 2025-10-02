import boto3
import csv
import json
from io import StringIO
from datetime import datetime

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ProcessedData')

def lambda_handler(event, context):
    # 1. Get bucket and file name
    bucket = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    
    # 2. Fetch file content
    file_obj = s3.get_object(Bucket=bucket, Key=file_key)
    file_content = file_obj['Body'].read().decode('utf-8')
    
    # 3. Parse CSV
    csv_data = csv.DictReader(StringIO(file_content))
    
    # 4. Process each row
    for row in csv_data:
        item = {
            'id': row.get('id') or str(datetime.utcnow().timestamp()),
            'name': row.get('name'),
            'email': row.get('email'),
            'uploadedAt': datetime.utcnow().isoformat()
        }
        # 5. Save to DynamoDB
        table.put_item(Item=item)
    
    return {
        'statusCode': 200,
        'body': json.dumps('File processed successfully!')
    }
