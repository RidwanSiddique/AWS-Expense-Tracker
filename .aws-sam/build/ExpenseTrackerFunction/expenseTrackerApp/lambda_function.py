import json
import boto3
import uuid
from decimal import Decimal

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ExpenseTracker')

def get_next_user_id():
    response = table.update_item(
        Key={'CounterName': 'UserCounter'},
        UpdateExpression='SET counter = counter + :inc',
        ExpressionAttributeValues={':inc': 1},
        ReturnValues='UPDATED_NEW'
    )
    return response['Attributes']['counter']

def decimal_to_json_serializable(item):
    if isinstance(item, list):
        return [decimal_to_json_serializable(i) for i in item]
    if isinstance(item, dict):
        return {k: decimal_to_json_serializable(v) for k, v in item.items()}
    if isinstance(item, Decimal):
        if item % 1 == 0:
            return int(item)
        else:
            return float(item)
    return item

def get_expenses(user_id):
    response = table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key('UserID').eq(user_id)
    )
    items = response.get('Items', [])
    return decimal_to_json_serializable(items)

def lambda_handler(event, context):
    if event['httpMethod'] == 'POST':
        try:
            body = json.loads(event['body'])
            user_id = get_next_user_id()
            expense_id = uuid.uuid4().hex
            item = {
                'UserID': str(user_id),
                'ExpenseID': expense_id,
                'Date': body['Date'],
                'Category': body['Category'],
                'SubCategory': body['SubCategory'],
                'Description': body['Description'],
                'Cost': str(body['Cost']),
                'PaymentMethod': body['PaymentMethod'],
                'Location': body['Location']
            }

            table.put_item(Item=item)

            return {
                'statusCode': 201,
                'body': json.dumps({'message': 'Expense added successfully', 'ExpenseID': expense_id})
            }
        except Exception as e:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': str(e)})
            }

    elif event['httpMethod'] == 'GET':
        try:
            user_id = event['queryStringParameters']['userID']
            expenses = get_expenses(user_id)
            return {
                'statusCode': 200,
                'body': json.dumps(expenses)
            }
        except Exception as e:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': str(e)})
            }

    else:
        return {
            'statusCode': 405,
            'body': json.dumps({'error': 'Method not allowed'})
        }
