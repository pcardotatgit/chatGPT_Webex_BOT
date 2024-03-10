'''
    the main script
'''
from gpt import gpt
from webex_bot.webex_bot import WebexBot
import sys
from crayons import *
from get_init_variables import get_init_variables
import config as conf

WEBEX_BOT_TOKEN=conf.WEBEX_BOT_TOKEN
GPT_API_KEY=conf.GPT_API_KEY
GPT_URL=conf.GPT_URL
GPT_VERSION=conf.GPT_VERSION

if __name__ == "__main__":
    g_variables=get_init_variables()
    if conf.GPT_API_KEY=="":
        conf.GPT_API_KEY=g_variables[1]
    conf.GPT_URL=g_variables[2] 
    conf.WEBEX_BOT_TOKEN=g_variables[0]
    conf.GPT_VERSION=g_variables[3]
    print()
    print('GPT_API_KEY : ',conf.GPT_API_KEY)
    print('GPT_URL : ',conf.GPT_URL)
    print('BOT_ACCESS_TOKEN : ',conf.WEBEX_BOT_TOKEN)
    print('GPT_VERSION : ',conf.GPT_VERSION)
    print()
    #sys.exit()
    bot = WebexBot(conf.WEBEX_BOT_TOKEN)
    bot.commands.clear()    
    bot.add_command(gpt())
    bot.help_command = gpt()
    bot.run()