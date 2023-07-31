import json
import boto3


tableName = "PeerProject"
serverURL = "http://3.210.92.223"
client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(tableName)

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
        
def get_item(ip: str):
    response = client.query(
            TableName=tableName,
            KeyConditionExpression='ip = :val',
            ExpressionAttributeValues={
                ':val': {'S': ip}
            }
        )
    items = response.get('Items', [])
    return items
    
def update_item_count(ip: str):
    client.update_item(
        TableName=tableName,
        Key={'ip': {'S': ip}},
        UpdateExpression='SET #countAttr = #countAttr + :inc',
        ExpressionAttributeNames={'#countAttr': 'count'},
        ExpressionAttributeValues={':inc': {'N': '1'}}
    )
    
def lambda_handler(event, context):
    data = client.scan(TableName=tableName)
    
    try:
        request_body = json.loads(event['body'])
        ip_address = request_body['ip']
        
        item = get_item(ip_address)
        if(item):
            update_item_count(ip_address)
        else:
            create_item(ip_address)
        
        
    except:
        return {
        'statusCode': 200,
        'body': json.dumps({"message": "ip","messsage1" : "error in creating/getting item", "data": data}),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': serverURL,
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        }
    }
    
    
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
