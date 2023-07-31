import json
import boto3


tableName = "IPTable"
serverURL = "http://18.144.27.150"
client = boto3.client('dynamodb')


def create_item(ip: str):
    #client.get_item(TableName=tableName, Key={"ip": {'S': ip}})
    # client.update_item(
    #     TableName = tableName
    #     Key={"IP": ip_to_increment},
    #     UpdateExpression="SET #countAttr = #countAttr + :inc",
    #     ExpressionAttributeNames={"#countAttr": "count"},
    #     ExpressionAttributeValues={":inc": 1}
    # )   
  
    client.put_item(TableName=tableName,Item={"ip": {'S': ip}, 'count': {'N': "1"}})
        

def lambda_handler(event, context):
    request_body = json.loads(event['body'])
    
    ip_address = request_body['ip']

    create_item(ip_address)

    data = client.scan(TableName=tableName)
    
    return {
        'statusCode': 200,
        'body': json.dumps(data),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': serverURL,
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        }
    }
