import boto3
client = boto3.client('s3')

response = client.put_object(
    Body='blah',
    Bucket='ztest1411',
    Key='byboto'
)
