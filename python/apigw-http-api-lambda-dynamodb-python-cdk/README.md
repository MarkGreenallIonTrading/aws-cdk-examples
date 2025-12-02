
# AWS API Gateway HTTP API to AWS Lambda in VPC to DynamoDB CDK Python Sample!


## Overview

Creates an [AWS Lambda](https://aws.amazon.com/lambda/) function writing to [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and invoked by [Amazon API Gateway](https://aws.amazon.com/api-gateway/) REST API. 

![architecture](docs/architecture.png)

## Security and Logging

This application implements comprehensive logging aligned with AWS Well-Architected Framework **SEC04-BP01: Configure service and application logging**:

### Logging Components

- **CloudTrail**: Captures all API activity across AWS services for audit and compliance
- **VPC Flow Logs**: Records network traffic for security investigations and troubleshooting
- **API Gateway Access Logs**: Logs all API requests with caller identity, IP, and response details
- **Lambda Function Logs**: Includes request ID, source IP, and operation details for security context
- **DynamoDB Point-in-Time Recovery**: Enables audit trails of data changes

### Log Retention

All logs are retained for **1 month** by default. CloudTrail logs in S3 are retained indefinitely for compliance.

### Accessing Logs

- **CloudWatch Logs**: Navigate to CloudWatch → Log groups
  - `/aws/lambda/apigw_handler` - Lambda function logs
  - VPC Flow Logs group - Network traffic logs
  - API Gateway access logs group - API request logs
- **CloudTrail**: Navigate to CloudTrail → Event history or query the S3 bucket
- **CloudWatch Logs Insights**: Use for querying and analyzing logs across log groups

## Setup

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Deploy
At this point you can deploy the stack. 

Using the default profile

```
$ cdk deploy
```

With specific profile

```
$ cdk deploy --profile test
```

## After Deploy
Navigate to AWS API Gateway console and test the API with below sample data 
```json
{
    "year":"2023", 
    "title":"kkkg",
    "id":"12"
}
```

You should get below response 

```json
{"message": "Successfully inserted data!"}
```

## Cleanup 
Run below script to delete AWS resources created by this sample stack.
```
cdk destroy
```

**Note**: CloudTrail S3 bucket is retained after stack deletion for compliance purposes.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
