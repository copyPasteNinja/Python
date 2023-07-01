import json, boto3
from urllib import response

# def lambda_handler(event, context):

    

def get_response():
    client = boto3.resource("dynamodb")
    table = client.Table("transactionsTest")
    clients = table.scan()
    
    # for trans in clients['Items']: 
    #     if trans['type'] == 

    transactionResponse = {}
    transactionResponse['transactionId'] = int(clients['Items'][0]['id'])
    transactionResponse['type'] = clients['Items'][0]['type']
    transactionResponse['amount'] = int(clients['Items'][0]['amount'])
    transactionResponse['message'] = "Hello from Lambda Land"

    # 3 Construct http response object 
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json' 
    responseObject['body'] = json.dumps(transactionResponse)

    return responseObject



   ################# WORKING ##################


# import json, boto3
# from urllib import response

# def lambda_handler(event, context):
    
#     # client = boto3.resource("dynamodb")
#     # table = client.Table("transactionsTest")
#     # clients = table.scan()
#     # print(clients)

    
#     print("----------------------------------------")
#     # 1 Parse out query strings params 
#     transactionId = event['queryStringParameters']['transactionId']
#     transactionType = event['queryStringParameters']['type']
#     transactionAmount = event['queryStringParameters']['amount']

#     print('transactionId=' + transactionId)
#     print('transactionType=' + transactionType)
#     print('transactionAmount=' + transactionAmount)

#     # 2 Construct the body of the respose
#     transactionResponse = {}
#     transactionResponse['transactionId'] = transactionId
#     transactionResponse['type'] = transactionType
#     transactionResponse['amount'] = transactionAmount
#     transactionResponse['message'] = "Hello from Lambda Land"

#     # 3 Construct http response object 
#     responseObject = {}
#     responseObject['statusCode'] = 200
#     responseObject['headers'] = {}
#     responseObject['headers']['Content-Type'] = 'application/json' 
#     responseObject['body'] = json.dumps(transactionResponse)

#     return responseObject
    