import boto3

# boto3 is the AWS SDK library for Python.
# The "resources" interface allow for a higher-level abstraction than the low-level client interface.
# More details here: http://boto3.readthedocs.io/en/latest/guide/resources.html
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Council')


# The BatchWriteItem API allows us to write multiple items to a table in one request.
with table.batch_writer() as batch:
    batch.put_item(Item={"Zipcode": "08550", "City": "West Windsor", "Person": "Allison Miller", "Position": "Council President", "Policy": { "Affiliation": "Democrat", "Beliefs": "D7YF4FCX" } })
    batch.put_item(Item={"Zipcode": "08550", "City": "West Windsor", "Person": "Yingchao (YZ) Zhang", "Position": "Council Vice President", "Policy": { "Affiliation": "Democrat", "Beliefs": "D7YF4FCX" } })
    batch.put_item(Item={"Zipcode": "08550", "City": "West Windsor", "Person": "Virginia Manzari", "Position": "Council Member", "Policy": { "Affiliation": "Democrat", "Beliefs": "D7YF4FCX" } })
    batch.put_item(Item={"Zipcode": "08550", "City": "West Windsor", "Person": "Linda Geevers", "Position": "Council Member", "Policy": { "Affiliation": "Democrat", "Beliefs": "D7YF4FCX" } })
