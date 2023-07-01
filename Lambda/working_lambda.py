import json, boto3, pprint, ast
from urllib import response
from decimal import *
from boto3.dynamodb.conditions import Key, Attr




# def drivers(driverName):
#     client = boto3.resource("dynamodb")
#     table = client.Table("DriverTable")
#     clients = table.scan()
#     # print(clients)
#     for driver in clients['Items']: 
        
#         if driver['driver'] == driverName:
#             result = driver
#         else:
#             result = {'error': 'Driver not found'}
#     return result

# print(drivers(driverName='JohnDoe'))


def load_search():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('DriverTable')
    
    response = table.query(KeyConditionExpression=Key('driver').eq('AbdulSharif'))
    print(len(response['Items']))
    # for load in response['Items']:
    #     print(len(load['']))


load_search()


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
    
    