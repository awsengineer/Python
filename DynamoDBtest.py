import boto3
from itertools import count

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('test-DynamoDBStack-B67ZSQ2FKLWX-DDBTable-B1GNHBVC9KP8')

response = table.put_item(
   Item={
        'fname': 'Nava',
        'lname': 'Salehi',
        'address': 'Melbourne VIC 3073'
    }
)

all_items = table.scan() 

for i in all_items['Items']:
    fname = i['fname']
    lname = i['lname']
    address = i['address']
    print (fname + " " + lname + " " + address)
