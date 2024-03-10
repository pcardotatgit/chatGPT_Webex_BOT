'''
    resource script dedicated to Webex Message and GPT Interaction
'''
from webex_bot.models.command import Command
from webex_bot.models.response import Response
import requests
import sys
import json
from crayons import *
from get_init_variables import get_init_variables
import config as conf


def get_global_variables():
    result={}

    if conf.GPT_API_KEY=="":
        result['GPT_API_KEY']=get_init_variables()[1]
    else:
        print('GPT_API_KEY already in memory')
        result['GPT_API_KEY']=conf.GPT_API_KEY
    if conf.GPT_URL=="":
        result['GPT_URL']=get_init_variables()[2]
    else:
        print('GPT_URL already in memory')
        result['GPT_URL']=conf.GPT_URL
    if conf.WEBEX_BOT_TOKEN=="":
        result['WEBEX_BOT_TOKEN']=get_init_variables()[0]  
    else:
        print('WEBEX_BOT_TOKEN already in memory')
        result['WEBEX_BOT_TOKEN']=conf.WEBEX_BOT_TOKEN
    if conf.GPT_VERSION=="":
        result['GPT_VERSION']=get_init_variables()[3]  
    else:
        print('GPT_VERSION already in memory')
        result['GPT_VERSION']=conf.GPT_VERSION        
    return(result)
  
class gpt(Command):
    messages=[]
    messages.append({"role":"system","content":"some content here"})
    
    def __init__(self):
        super().__init__()
        
    def execute(self, message, attachment_actions, activity):
        #return "Hello World"
        if conf.GPT_API_KEY=="":
            conf.GPT_API_KEY=get_global_variables()['GPT_API_KEY']
        else:
            print('GPT_API_KEY already in memory')            
        if conf.GPT_URL=="":
            conf.GPT_URL=get_global_variables()['GPT_URL']
        else:
            print('GPT_URL already in memory')            
        print("====AA >====")
        print('GPT_API_KEY : ',conf.GPT_API_KEY)
        print('GPT_URL : ',conf.GPT_URL)
        print("====< AA====")           
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json','Authorization': "Bearer "+conf.GPT_API_KEY}
        messages=[]
        messages.append({"role":"user","content":message})
        payload={
            "model":conf.GPT_VERSION,
            "messages":messages            
        }
        response = requests.post(conf.GPT_URL, headers=headers,data=json.dumps(payload))
        print()
        print('json response :\n',cyan(response.json(),bold=True))
        print()
        #sys.exit()
        rep=json.dumps(response.json())
        gpt_response=response.json()['choices'][0]['message']['content']
        print()
        print(gpt_response)
        print()
        messages.append({"role":"assistant","content":message})
        return gpt_response      

      