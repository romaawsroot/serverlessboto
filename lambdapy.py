import boto3
def handler(event, context):
    client = boto3.client('s3')
    response = client.create_bucket(
    Bucket='examplebucket77romaawsrozoro5',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-1',},
    )
    return {"message": "hi there"}
