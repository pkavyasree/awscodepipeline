import boto3
import json

ec2 = boto3.client('ec2')
def lambda_handler(event, context):
    message = 'Hello {} {}!'.format(event['blue'], 
                                    event['skies'])  
    return { 
        'message' : message
    }
    
