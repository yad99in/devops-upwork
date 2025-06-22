import boto3
from datetime import datetime, timedelta

s3 = boto3.client('s3')

def cleanup_old_files(bucket, days=30):
    cutoff = datetime.now() - timedelta(days=days)
    objects = s3.list_objects_v2(Bucket=bucket)['Contents']
    for obj in objects:
        if obj['LastModified'] < cutoff:
            s3.delete_object(Bucket=bucket, Key=obj['Key'])

cleanup_old_files("my-backup-bucket")
