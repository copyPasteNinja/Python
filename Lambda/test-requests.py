#!/usr/bin/env python3

import requests, json, os, boto3, pprint, ast
from decimal import *
from boto3.dynamodb.conditions import Key, Attr
pp = pprint.PrettyPrinter(indent=4)


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        # 👇️ if passed in object is instance of Decimal
        # convert it to a string
        if isinstance(obj, Decimal):
            return str(obj)
        # 👇️ otherwise use the default behavior
        return json.JSONEncoder.default(self, obj)

# dynamodb = boto3.resource('dynamodb')

# table = dynamodb.Table('transactionsTest')

# response = table.scan()
# response['Items']

# print(response)

##################################################

# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('transactionsTest')
# response = table.get_item(
#     Key={
#         'deliveryDate': {'S': '02/22/2021'},
#         'destination': {'S': 'San Diego, CA'},
#         'driver': {'S': 'RejabaliSharif'},
#         'id': {'N': '2'},
#         'loadNumber': {'S': '12345CBA'},
#         'miles': {'S': '1050'},
#         'origin': {'S': 'Mount Prospect, IL'},
#         'pickUpdate': {'S': '02/22/2021'},
#         'rate': {'S': '3499'},
#         'secondDdate': {'S': 'Null'}
#         }
# )
# print(response['Item'])


#######################################
# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('transactionsTest')

# response = table.scan(FilterExpression=Attr('driver').eq('DovudSharif'))
# for i in response['Items']:
#     d = ast.literal_eval((json.dumps(i, cls=DecimalEncoder)))

# print(d)

#########################################

client = boto3.resource("dynamodb")
table = client.Table("transactionsTest")
clients = table.scan()

test = []
for i in clients['Items']:
    load_data = ast.literal_eval((json.dumps(i, cls=DecimalEncoder)))
    test.append(load_data)

print(test)