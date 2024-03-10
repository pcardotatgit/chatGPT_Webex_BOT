# chatGPT Webex BOT 

This project is a basic chatGPT webex bot that allows users to interact with chatGPT thru a webex room

It is given as a proof of concept, as a code template that has the goal to make you understand how to build it.

You will see that it doesn't depend on the openai python module, but use raw APIs. Which helps to better understand what we do at the basic level.

# Pre requisits

First, You must have a Webex Bot.

Follow the instructions here in order to create one : [Create_a_Webex_bot_for_XDR_Alerts](https://github.com/pcardotatgit/Create_a_Webex_bot_for_XDR_Alerts)

Second You must have an account to OPENAI ( at openai.com ) and you must have created an API key.

**Notice** : the script work with a GPT version you would have installed into a local server. If so, then change the GPT_URL into the config.txt file

## Run the bot

First edit the **config.txt** file and assign the correct values to the empty variables.  DON'T USE QUOTES ! in the variable declarations !!

From a CMD console openned into the application folder into your laptop run the app.y script :

    python app.py

Then go to your Webex client and open a conversation with the bot if not already done.

Then send : **Hello**.

You are supposed to receive an **Hello, How can I help You today** answer from the Bot.

Then you can chat with it.

You can check the conversation into the bot console


## Installation

Installing these scripts is pretty straight forward . You can just copy  and paste them into your python environment but a good practice is to run them into a python virtual environment.

If dont have your python environment yet, basically you just need a python interpreter ( 3.7 is enough but 3.11 is better ). For windows users google search for **Python for windows** and install it. Don't forget to click on the **add to path** check box. And that's it.

Cisco DEVNET provide you with very good resources about the tools to install into your latop in order to build your development workstation.

Go to for example to [ Developer Workstation and Environment Setup ](https://developer.cisco.com/learning/tracks/devnet-express-security-v1-1/dev-setup/)

Select your Operating System and go thru the instructions.

All recommended tools in the DEVNET Section is good to install.

### Step 1 - Create a working directory into your laptop

Create a working directory into your laptop ( ex : chatGPT_Webex_BOT ) and open a terminal console into it. 

You will put all code into this working directory

### Step 2 - Create a Python virtual environment and start it

**Create a virtual environment on Windows**

	python -m venv venv 
    
**Create a virtual environment on Linux or Mac**

	python3 -m venv venv

    Depending on the python version you installed into your Mac you might have to type either 

    - python -m venv venv

    or maybe

    - python3 -m venv venv    : python3 for python version 3.x  

    or maybe 

    - python3.9 -m venv venv  : if you use the 3.9 python version

And then move to the next step : Activate the virtual environment.

**Activate the virtual environment on Windows**

	venv\Scripts\activate
    
**Activate the virtual environment on Linux or Mac**

	source venv/bin/activate    

### Step 3 - clone the scripts into your laptop

**> If you have a git client** 

If you have a git client you can use the following command :

	git clone https://github.com/pcardotatgit/chatGPT_Webex_BOT.git
	cd chatGPT_Webex_BOT/

**> Or if you DON'T have a git client** 

You can download the zip package by clicking on the **clone** button on the top right of this git page. Click on **download.zip**. And then unzip the zip file into your working directory. 

### Step 4 -Install needed modules

The scripts need the following python modules

- requests
- crayons
- webex_bot

You can install them with the following  ( Windows / Mac / Linux ) :
	
	python -m pip install --upgrade pip  ( this command is only needed if your python version is old and if the secod command fails )
	pip install -r requirements.txt

Or you can install required modules separatly :
	
	python -m pip install --upgrade pip
	pip install requests
	pip install crayons
	pip install webex_bot

**Done ! you are ready to run the bot**

## You want to extend conversation capabilities with your webex bot

This Proof Of Concept use only chatGPT as conversation backend.   You can extend your bot behaviors in order to make it react differentle depending on which messages are send into the Webex Room.

For doing so , then edit the **gpt.py** script and go to the **exexute(..)** function into the **gpt()** class. At this location you can add some if statements that check the messages that are send by users into the room ( and then trigger customized actions ).

The variable to check here is the **message** variable. 