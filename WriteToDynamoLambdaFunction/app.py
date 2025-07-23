import os
import csv
import boto3
from aws_lambda_powertools import Tracer  # Add this line

env_table = os.environ['TABLE']

s3 = boto3.client('s3')
unzipped_s3_prefix = "unzipped/"
dynamodb = boto3.resource('dynamodb')
ddb_table = dynamodb.Table(env_table)

tracer = Tracer()  # Add this line

def parse_csv_ddb(app_uuid, details_file):
    "Load CSV and save to dynamo"
    with open(details_file, 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        details_dict = next(reader)

    ddb_table.put_item(Item={**details_dict, "APP_UUID": app_uuid})

    return details_dict

@tracer.capture_lambda_handler  # Add this line
def lambda_handler(event, context):
    "Called from step functions to load CSV to DynamoDB"
    bucket = event['detail']['bucket']['name']
    app_uuid = event['application']['app_uuid']
    details_key = f"{unzipped_s3_prefix}{app_uuid}_details.csv"
    details_file = f"/tmp/{app_uuid}_details.csv"

    s3.download_file(bucket, details_key, details_file)
