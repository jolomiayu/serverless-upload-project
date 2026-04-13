import json
import boto3
import os
import uuid

s3 = boto3.client('s3', region_name='eu-west-1')

BUCKET = os.environ['BUCKET_NAME']

def lambda_handler(event, context):

    path = event.get("rawPath", "")

    # UPLOAD URL
    if path.endswith("/upload-url"):
        file_name = str(uuid.uuid4())

        url = s3.generate_presigned_url(
            'put_object',
            Params={
                'Bucket': BUCKET,
                'Key': file_name,
                'ContentType': 'application/octet-stream'
            },
            ExpiresIn=300
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'uploadUrl': url,
                'fileName': file_name
            })
        }

    # DOWNLOAD URL
    elif path.endswith("/download-url"):

        params = event.get("queryStringParameters") or {}
        file_name = params.get("fileName")

        if not file_name:
            return {
                'statusCode': 400,
                'body': json.dumps({"error": "fileName is required"})
            }

        url = s3.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': BUCKET,
                'Key': file_name
            },
            ExpiresIn=300
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'downloadUrl': url
            })
        }

    return {
        'statusCode': 404,
        'body': json.dumps({"message": "Not Found"})
    }