import boto3
import json

ec2 = boto3.client('ec2',region_name="us-east-1",aws_access_key_id="AKIAIUIGD4R2ZEXJUP5A",aws_secret_access_key="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")
def lambda_handler(event, context):
    response = ec2.describe_availability_zones()
    return {"statusCode": 200, "body": json.dumps(response)}
