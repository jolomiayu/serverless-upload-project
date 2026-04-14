import json
import boto3
import os
import uuid

s3 = boto3.client('s3', region_name='eu-west-1')
BUCKET = os.environ['BUCKET_NAME']

def lambda_handler(event, context):
    print("Incoming event:", event)

    # 🔥 FORCE ERROR
    1/0

    path = event.get("rawPath", "")

    return {
        'statusCode': 200,
        'body': json.dumps({"message": "test"})
    }
