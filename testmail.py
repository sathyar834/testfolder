import json
import time
import re
import boto3
from flask import Flask,jsonify,request
client = boto3.client('organizations')

def createacc():
  list_of_Emails = ["sathyar834@gmail.com","sat@ggf","finalmail@aws.com"]
  list_of_Names = ["ssss","yyyy","finalmail"]
  Existing_emails = ["safgh@gmail.com","sathyar834@gmail.com"]
  for mail,name in zip(list_of_Emails,list_of_Names):
    for awsmail in Existing_emails:
      mailstatus = bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", mail))
      if mailstatus == True:
        if mail == awsmail:
          status = "Invalid email"
          print("The email",mail,"already exist!")
          break
        else:
          status = "Valid email"
      else:
        print("The email format is Invalid for",mail)
        break
    if status == "Valid email":
      # cresponse = client.create_account(
      #   Email= mail,
      #   AccountName= name,
      #   IamUserAccessToBilling='ALLOW'
      # )
      print("Account created successfully")


createacc()