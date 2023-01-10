import boto3
import os

# S3 Connection configuration
config = {
    "aws_access_key_id": "",
    "aws_secret_access_key": "",
    "endpoint_url": "",
}

# Vars
save_bucket = "world-backup"
backup_file_location = "/home/wurmatron/backup/backup.tar.gz"
prefix = "backup"

client = boto3.client("s3", **config)

# Check for backup bucket
found = False
response = client.list_buckets()
for bucket in response['Buckets']:
    if bucket['Name'] == save_bucket:
        found = True
        print("Found bucket '" + save_bucket + "'")

# Create bucket if one does not exist
if not found:
    client.create_bucket(Bucket=save_bucket)
    print("Bucket '" + save_bucket + "' not found, creating!")

name = os.path.basename(backup_file_location).split('/')[-1]
# # Check if file exists
# response = client.list_objects(Bucket=save_bucket)
# try:
#     for a in response['Contents']:
#         if a['Key'] == prefix + "/" + name:
#             print("Old File exists!")
# except:
#     print("Cannot find files, assuming its empty")

# Upload
print("Uploading '" + backup_file_location + "' as '" + save_bucket + "#" + prefix + "/" + name)
client.upload_file(
    Filename=backup_file_location,
    Bucket=save_bucket,
    Key=prefix + "/" + name)

print("Completed!")
