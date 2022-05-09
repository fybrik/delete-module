import requests
import boto3

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))
print("Changed")
s3_resource = boto3.resource("s3", endpoint_url="http://127.0.0.1:4566", aws_access_key_id="1234", aws_secret_access_key="1234")