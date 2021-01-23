import json
import boto3
from botocore.exceptions import ClientError

client = boto3.client('organizations')

# class Error(Exception):
#   pass

def moveacc():
  try:
    Create_OU_response = client.create_organizational_unit(
    ParentId= 'ou-oblp-orfz456',
    Name='yes'
    )
  except ClientError as e:
    raise e

moveacc()