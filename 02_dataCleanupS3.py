import boto3
from datetime import datetime, timezone, timedelta

def lambda_handler(event, context):
    # Initialize the S3 client
    s3_client = boto3.client('s3')
    
    # Define the S3 bucket
    bucket_name = 'arpit-image-compr-s3'  # Replace with your bucket name
    
    # Set the files deletion cutoff date to 30 days
    days_old = 7   # For testing purpose, keeping it to 7 days
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=days_old)
    
    # List objects in the bucket
    objects = s3_client.list_objects_v2(Bucket=bucket_name)
    
    if 'Contents' in objects:
        for obj in objects['Contents']:
            object_key = obj['Key']
            last_modified = obj['LastModified']
            
            # Delete the files that are older than the cutoff date
            if last_modified < cutoff_date:
                s3_client.delete_object(Bucket=bucket_name, Key=object_key)
                print(f"Deleted {object_key}, last modified: {last_modified}")
            else:
                print(f"Retained {object_key}, last modified: {last_modified}")
    else:
        print("Bucket is either empty or no objects found.")
    
    return {
        'statusCode': 200,
        'body': 'Automated S3 Bucket Cleanup completed!'
    }
