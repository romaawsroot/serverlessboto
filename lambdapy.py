import boto3

def lambdapy(event, context):

    client = boto3.client('s3')

    response = client.create_bucket(
    Bucket='examplebucket',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2',},
    )
