import boto3
def handler(event, context):
    client = boto3.client('s3')
    response = client.create_bucket(
    Bucket='examplebucket77romaawsrozoro22118899889988zoro11144',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2',},
    )
    return {"message": "hi there"}
