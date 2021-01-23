# import json
# from pynput.keyboard import Key, Controller as KeyboardController
# from pynput.mouse import Button, Controller as MouseController

# def mouse():
#   mouse = MouseController()
#   # print ("Current position: " + str(mouse.position))
#   mouse.position = (1032, 20)
# mouse()
from pynput import mouse
import json
import boto3

client = boto3.client('iam')

class MyException(Exception): pass

def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        raise MyException(button)

# Collect events until released
with mouse.Listener(
        on_click=on_click) as listener:
    try:
        listener.join()
    except MyException as e:
        print('{0} was clicked'.format(e.args[0]))
        # response = client.delete_access_key(
        # UserName='STSAssumeUser',
        # AccessKeyId='AKIAUWY2OTUPXHV5NOHE'
        # )
        # print(response)
