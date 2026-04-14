import json
import boto3
import os
import uuid

s3 = boto3.client('s3', region_name='eu-west-1')
BUCKET = os.environ['BUCKET_NAME']

def lambda_handler(event, context):
    print("Incoming event:", event)
    
    path = event.get("rawPath", "")
    print("Request path:", path)

    # =========================
    # UPLOAD URL
    # =========================
    if path.endswith("/upload-url"):
        file_name = str(uuid.uuid4())
        print("Generated file name:", file_name)

        url = s3.generate_presigned_url(
            'put_object',
            Params={
                'Bucket': BUCKET,
                'Key': file_name,
                'ContentType': 'application/octet-stream'
            },
            ExpiresIn=300
        )

        print("Generated upload URL")

        return {
            'statusCode': 200,
            'body': json.dumps({
                'uploadUrl': url,
                'fileName': file_name
            })
        }

    # =========================
    # DOWNLOAD URL
    # =========================
    elif path.endswith("/download-url"):
        params = event.get("queryStringParameters") or {}
        file_name = params.get("fileName")

        print("Download request for file:", file_name)

        if not file_name:
            print("Error: fileName missing")
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

        print("Generated download URL")

        return {
            'statusCode': 200,
            'body': json.dumps({
                'downloadUrl': url
            })
        }

    print("Invalid route hit")

    return {
        'statusCode': 404,
        'body': json.dumps({"message": "Not Found"})
    }
