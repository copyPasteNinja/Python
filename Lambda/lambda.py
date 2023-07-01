#!/usr/bin/env python3

import json, boto3, pprint, ast
from urllib import response
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

def load_search(driver):
    loads = []
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('transactionsTest')
    response = table.scan(FilterExpression=Attr('driver').eq(driver))
    pp.pprint(response)
    if len(response['Items']) == 0:
        transactionResponse = {'Error': 404}
        loads.append(transactionResponse)
    else:
        for item in response['Items']:
            transactionResponse = {}
            transactionResponse['id'] = int(item['id'])
            transactionResponse['driver'] = str(item['driver']) 
            transactionResponse['deliveryDate'] = str(item['deliveryDate'])
            transactionResponse['pickUpdate']  = str(item['pickUpdate'])
            transactionResponse['origin'] = str(item['origin'])
            transactionResponse['rate'] = int(item['rate'])
            transactionResponse['destination'] = str(item['destination'])
            transactionResponse['secondDdate'] = str(item['secondDdate'])
            transactionResponse['loadNumber']  = str(item['loadNumber'])
            transactionResponse['miles'] = int(item['miles'])
            loads.append(transactionResponse)
    return loads

load_search('DovudSharif')


def request_handler(event):
    client = boto3.resource("dynamodb")
    table = client.Table("transactionsTest")
    clients = table.scan()
    if len(event['pathParameters']['loads'].split('/')) == 2:
        driver = event['pathParameters']['loads'].split('/')[1]
        load_query = json.dumps(load_search(driver))
        transactionResponse = load_query
            # transactionResponse = {} #{'response': event['queryStringParameters']['type']}
            # transactionResponse['id'] = int(item['id'])
            # transactionResponse['driver'] = item['driver']
            # transactionResponse['deliveryDate'] = item['deliveryDate']
            # transactionResponse['pickUpdate'] = item['pickUpdate']
            # transactionResponse['origin'] = item['origin']
            # transactionResponse['rate'] = int(item['rate'])
            # transactionResponse['destination'] = item['destination']
            # transactionResponse['secondDdate'] = item['secondDdate']
            # transactionResponse['loadNumber'] = item['loadNumber']
            # transactionResponse['miles'] = int(item['miles'])
    else:
        transactionResponse = []
        for i in clients['Items']:
            load_data = ast.literal_eval((json.dumps(i, cls=DecimalEncoder)))
            transactionResponse.append(load_data)
        #transactionResponse = {'error': 'Driver not found'}
    
    return transactionResponse
    # driver = event['pathParameters']['loads'].split('/')[1]
    # print(event['pathParameters']['loads'].split('/'))
    # print('Path Param is ' + driver)


def lambda_handler(event, context):
    
    transactionResponse = request_handler(event=event)
    # 3 Construct http response object 
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json' 
    responseObject['body'] = json.dumps(transactionResponse)
    
    
    
    return responseObject
    
    