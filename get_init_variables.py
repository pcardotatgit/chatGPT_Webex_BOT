'''
    this script is dedicated to read config.txt file and initializa super global variables
'''
import requests
import sys
import json
from crayons import *

def get_init_variables():
    with open('config.txt','r') as file:
        text_content=file.read()
    text_lines=text_content.split('\n')
    conf_result=[]
    value=""
    for line in text_lines:
        print(green(line,bold=True))
        if 'GPT_API_KEY' in line:
            words=line.split('=')
            if len(words)==2:
                value=line.split('=')[1]
                value=value.replace('"','')
                value=value.replace("'","")
            else:
                value="" 
            conf_result.append(value)
        if 'GPT_URL' in line:
            words=line.split('=')
            if len(words)==2:
                value=line.split('=')[1]
                value=value.replace('"','')
                value=value.replace("'","")
            else:
                value=""
            conf_result.append(value)
        if 'WEBEX_BOT_TOKEN' in line:
            words=line.split('=')
            if len(words)==2:
                value=line.split('=')[1]
                value=value.replace('"','')
                value=value.replace("'","")
            else:
                value=""
            conf_result.append(value)
        if 'GPT_VERSION' in line:
            words=line.split('=')
            if len(words)==2:
                value=line.split('=')[1]
                value=value.replace('"','')
                value=value.replace("'","")
            else:
                value=""
            conf_result.append(value)            
    print()
    print('Init global variables :\n', yellow(conf_result))
    print()
    return conf_result        