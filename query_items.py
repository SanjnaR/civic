import boto3
from boto3.dynamodb.conditions import Key

# boto3 is the AWS SDK library for Python.
# The "resources" interface allows for a higher-level abstraction than the low-level client interface.
# For more details, go to http://boto3.readthedocs.io/en/latest/guide/resources.html
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Council')

# When making a Query API call, we use the KeyConditionExpression parameter to specify the hash key on which we want to query.
# We're using the Key object from the Boto3 library to specify that we want the attribute name ("Author")
# to equal "John Grisham" by using the ".eq()" method.

#query zipcodes to get cities
zipcode = str(input('Enter your zipcode: '))
resp = table.query(KeyConditionExpression=Key('Zipcode').eq(zipcode))
print("The query returned the following items:")


people = []
for item in resp['Items']:
    people.append(item['Person'])
    
res = [i for n, i in enumerate(people) if i not in people[:n]] 
print(res)

person = str(input('Please pick a person from the list above: '))
#resp = table.query(KeyConditionExpression=Key('Person').eq(person))

resp = table.get_item(Key={"Zipcode": zipcode, "Person": person})
print(resp["Item"])