import boto3
def handler(event, context):
    client = boto3.client('s3')
    response = client.create_bucket(
    Bucket='bucketname',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2',},
    )
    return {"message": "hi there"}
