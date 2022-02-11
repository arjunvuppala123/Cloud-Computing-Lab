import json

def lambda_handler(event, context):
    toBeDumped = ""
    if event["requestContext"]["http"]["method"] == "GET":
        toBeDumped = "pes2ug19cs451 : " + event["queryStringParameters"]["key"]
    else:
        toBeDumped = "Only GET is supported"
    return {
        'statusCode': 200,
        'body': json.dumps(toBeDumped)
    }