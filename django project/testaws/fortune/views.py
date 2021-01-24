from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
import json
import boto3

client = boto3.client('organizations')
# Create your views here.
# request = "this is satya"
event = {
  "a":"r-oblp",
  "b":"django"
}


@api_view(['POST'])
def fortune(request):

  event= request.data
  x= event["a"]
  y= event["b"]

  if request.method == 'POST':
    Create_OU_response = client.create_organizational_unit(
    ParentId= x,
    Name=y
    )
    print(Create_OU_response)
    return("created")