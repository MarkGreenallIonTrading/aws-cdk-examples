# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()

import boto3
import os
import json
import logging
import uuid

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb_client = boto3.client("dynamodb")


def handler(event, context):
    table = os.environ.get("TABLE_NAME")
    request_id = context.request_id
    source_ip = event.get("requestContext", {}).get("identity", {}).get("sourceIp", "unknown")
    
    logging.info(f"Request ID: {request_id}, Source IP: {source_ip}, Table: {table}")
    
    try:
        if event.get("body"):
            item = json.loads(event["body"])
            logging.info(f"Request ID: {request_id}, Processing payload with id: {item.get('id', 'N/A')}")
            year = str(item["year"])
            title = str(item["title"])
            id = str(item["id"])
            
            dynamodb_client.put_item(
                TableName=table,
                Item={"year": {"N": year}, "title": {"S": title}, "id": {"S": id}},
            )
            
            logging.info(f"Request ID: {request_id}, Successfully inserted data for id: {id}")
            message = "Successfully inserted data!"
            return {
                "statusCode": 200,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"message": message}),
            }
        else:
            logging.info(f"Request ID: {request_id}, No payload provided, using default data")
            default_id = str(uuid.uuid4())
            
            dynamodb_client.put_item(
                TableName=table,
                Item={
                    "year": {"N": "2012"},
                    "title": {"S": "The Amazing Spider-Man 2"},
                    "id": {"S": default_id},
                },
            )
            
            logging.info(f"Request ID: {request_id}, Successfully inserted default data with id: {default_id}")
            message = "Successfully inserted data!"
            return {
                "statusCode": 200,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"message": message}),
            }
    except Exception as e:
        logging.error(f"Request ID: {request_id}, Error processing request: {str(e)}", exc_info=True)
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "Internal server error"}),
        }
