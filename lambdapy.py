import boto3
def handler(event, context):
    client = boto3.client('s3')
    response = client.create_bucket(
    Bucket='examplebucketromaawsrozoro22118899889988zoro',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2',},
    )
    return {"message": "hi there"}
