import boto3
from io import BytesIO

output_bucket = 'henryvstone-ending-files'

s3 = boto3.client('s3', use_ssl=True)

def handler(event, context):
    output_bucket = 'henryvstone-ending-files'

    key = event['Records'][0]['s3']['object']['key']
    input_bucket = event['Records'][0]['s3']['bucket']['name']

    s3.upload_fileobj(                      # upload a new obj to s3
    Fileobj=BytesIO(s3.get_object(Bucket=input_bucket, Key=key)['Body'].read()),
    Bucket=output_bucket,                      # target bucket, writing to
    Key=key)               # target key, writing to
