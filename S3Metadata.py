import boto3
from itertools import count

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-2')
table = dynamodb.Table('S3Metadata')

all_items = table.scan() 

for i in all_items['Items']:
    customer_name = i['customer_name']
    key = i['key']
    object_modified_date = i['object_modified_date']
    object_size = i['object_size']
    print (customer_name + " " + key + " " + object_modified_date + " " + str(object_size))

response = table.put_item(
   Item={
        'customer_name': 'company1',
        'key': '/bucket1/object1',
        'object_modified_date': '2018-02-03T04:47:18.000Z',
        'object_size': '35966'
    }
)

