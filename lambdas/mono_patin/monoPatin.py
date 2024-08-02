import json
import uuid

headers_open = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
    "Access-Control-Allow-Headers": "Content-Type"
}

# In-memory data storage
electric_scooters = []

def lambda_handler(event, context):
    method = event['httpMethod']

    if method == 'GET':
        return get_scooters(event)
    elif method == 'POST':
        return create_scooter(event)
    elif method == 'PUT':
        return update_scooter(event)
    elif method == 'DELETE':
        return delete_scooter(event)
    else:
        return {
            'statusCode': 405,
            'headers': headers_open,
            'body': json.dumps({'message': 'Method Not Allowed'})
        }


def get_scooters(event):
    return {
        'statusCode': 200,
        'headers': headers_open,
        'body': json.dumps(electric_scooters)
    }


def create_scooter(event):
    body = json.loads(event['body'])
    scooter = {
        'id': str(uuid.uuid4()),
        'marca': body['marca'],
        'modelo': body['modelo'],
        'velocidadMaxima': body['velocidadMaxima'],
        'autonomia': body['autonomia']
    }
    electric_scooters.append(scooter)
    return {
        'statusCode': 201,
        'headers': headers_open,
        'body': json.dumps(scooter)
    }


def update_scooter(event):
    body = json.loads(event['body'])
    scooter_id = event['pathParameters']['id']
    for scooter in electric_scooters:
        if scooter['id'] == scooter_id:
            scooter['marca'] = body['marca']
            scooter['modelo'] = body['modelo']
            scooter['velocidadMaxima'] = body['velocidadMaxima']
            scooter['autonomia'] = body['autonomia']
            return {
                'statusCode': 200,
                'headers': headers_open,
                'body': json.dumps(scooter)
            }
    return {
        'statusCode': 404,
        'headers': headers_open,
        'body': json.dumps({'message': 'Scooter not found'})
    }


def delete_scooter(event):
    scooter_id = event['pathParameters']['id']
    global electric_scooters
    electric_scooters = [scooter for scooter in electric_scooters if scooter['id'] != scooter_id]
    return {
        'statusCode': 204,
        'headers': headers_open
    }
