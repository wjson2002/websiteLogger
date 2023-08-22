import json
import boto3


tableName = "PeerProject"
serverURL = "http://3.210.92.223"
client = boto3.client('dynamodb')


def create_item(ip: str):
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
    client.update_item(
        TableName=tableName,
        Key={'ip': {'S': "-1"}},
        UpdateExpression='SET #countAttr = #countAttr + :inc',
        ExpressionAttributeNames={'#countAttr': 'count'},
        ExpressionAttributeValues={':inc': {'N': '1'}}
    )
    
def lambda_handler(event, context):
    data = client.scan(TableName=tableName)
    
    item_count = data['Count']
    ip_address = "-1"
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
        'body': json.dumps({"count": item_count,"messsage1" : "error in creating/getting item"}),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': serverURL,
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        }
    }
    
    return {
        'statusCode': 200,
        'body': json.dumps({"count": item_count,"yourIP": get_item(ip_address)}),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': serverURL,
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        }
    }
