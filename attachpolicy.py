import json
import time
import boto3

iamclient = boto3.client('iam')

def attachpolicy():
  data = "AdministratorAccess"
  # attachresponse = iamclient.attach_user_policy(
  #   UserName='Assume_role_user',
  PolicyArn='arn:aws:iam::aws:policy/{}'.format(data)
  print(PolicyArn)

attachpolicy()