# from pynput.mouse import Button, Controller as MouseController
# from pynput.keyboard import Key, Controller as KeyboardController
from pynput import mouse
from pynput import keyboard
import json
import boto3
# mouse = MouseController()
# keyboard = KeyboardController()
client = boto3.client('iam')
stsclient = boto3.client('sts')

def assumerole():
  # anotheraccountresponse = stsclient.assume_role(
  #   RoleArn="arn:aws:iam::689020024752:role/OrganizationAccountAccessRole",
  #   RoleSessionName='master_to_acess_VLG',
  # )
  # credentials=anotheraccountresponse['Credentials']
  # print(credentials)

  # access_key_id='ASIA2A3GLG6YDUYYZQTN',
  # secret_access_key='Nk5rDwkQqXbIp4y7P5NrKWrawB7OWb7NuWGN4q7S',
  # session_token='FwoGZXIvYXdzEBkaDIr2maYtueXJzK53wyK3Ab4LDVJAAqWtAE7dOmnyAAyOL9iTYB4Uv/TvzUEfUySkhs1ZyoLx/EFRsMELw9VbZ7JX8YOnU1/o94P1S8rVsudR8s1FJXOzp+I4QCPeLspk8xFyqhf4XGwaxF97LSNODDZbG4kj/BXVEeuUyNGfQXqrbzMep45LKgMCfeEOTVbexm6rtD7llnDyHs65dwOdw5H7GwNYaTYs7z5m8p5ur0CXw5kWa75jSqr8u0qFewLGFZRkvDv7byj5r8L/BTItKiJGeQ3Lvq+YAOuxu3p6X4e8/fAebjOXhI1TDPd8Fx4hxol7ls/U3nYhzLig',
  
  # iamclient = boto3.client(
  #   'iam',
  #   aws_access_key_id= 'ASIA2A3GLG6YDUYYZQTN',
  #   aws_secret_access_key= 'Nk5rDwkQqXbIp4y7P5NrKWrawB7OWb7NuWGN4q7S',
  #   aws_session_token= 'FwoGZXIvYXdzEBkaDIr2maYtueXJzK53wyK3Ab4LDVJAAqWtAE7dOmnyAAyOL9iTYB4Uv/TvzUEfUySkhs1ZyoLx/EFRsMELw9VbZ7JX8YOnU1/o94P1S8rVsudR8s1FJXOzp+I4QCPeLspk8xFyqhf4XGwaxF97LSNODDZbG4kj/BXVEeuUyNGfQXqrbzMep45LKgMCfeEOTVbexm6rtD7llnDyHs65dwOdw5H7GwNYaTYs7z5m8p5ur0CXw5kWa75jSqr8u0qFewLGFZRkvDv7byj5r8L/BTItKiJGeQ3Lvq+YAOuxu3p6X4e8/fAebjOXhI1TDPd8Fx4hxol7ls/U3nYhzLig',
  # )

  # Userresponse = iamclient.create_user(
  #   UserName='Assume_rolefi',
  # )
  # print(Userresponse)

  with keyboard.Events() as events:
    x=2
    while x==2:
      event = events.get(30.0)
      if event is None:
        print("sss")
        iamclient = boto3.client(
        'iam',
        aws_access_key_id= 'ASIA2A3GLG6YLVZDBIUK',
        aws_secret_access_key= 'ZPUUrQqSVCYQ8p6C4BUPxeAxTYllL9WJXhTpVCop',
        aws_session_token= 'FwoGZXIvYXdzEGkaDApsoCvMOLX2WSGqpiK3AW7Pe9I+lUELFGDS+lrbK5wmEtYg6i4kFH8ZBBsVc7Q2LzPKQL5ZSkE76EqyY+hIlcUGefpqYioV44yT4i8htSiPFmcnHVKBydqYYR+t3K68qn2sTDTihVAOwuhCsWO1go0PYRK8bsULqmDoYBYDFn1wSkmHlysAQo5gUnkz6SZ9yJMlSLndjWkLD0oH20QNfDgSCkvQnmtJaeo+NXnIC18SlEvNT2Ftv3iGqharyo83DfY9pqDTNCj0gYyABjItJk7WPpf138ueJpym0ybAbpLM9zeZ1fOJua7jx+kEFsVS59U0SSRK+SY+A6Et',
        )
        response = iamclient.detach_role_policy(
            RoleName='OrganizationAccountAccessRole',
            PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess'
        )
        print("deleted")
        break
      else:
        print('Received event {}'.format(event))

assumerole()

