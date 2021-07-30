# Preview

## Login Page
![image](https://user-images.githubusercontent.com/26377024/127664677-1516a101-5314-47ed-b2f1-308a885fdc4e.png)

When another user attempts to login with the same username

![image](https://user-images.githubusercontent.com/26377024/127664439-6c95fba3-e65c-4cfc-bdf6-e00b7b147d63.png)

## Chatbot

![image](https://user-images.githubusercontent.com/26377024/127665082-8321a5be-4902-46af-8494-9424962298b4.png)

## Logs

![image](https://user-images.githubusercontent.com/26377024/127665571-f9ba5317-8f61-43ee-80b9-9329e8cd208e.png)
  
   
   
      
    
---

# django-bot-server-tutorial

Accompanying repository for a seminar on creating a django based bot server that uses django-channels for  WebSockets connection. This borrows heavily from the code at https://github.com/andrewgodwin/channels-examples 

# What is this useful for?

- Get an idea how to get django-channels working
- Get some sample code for a simple working front end that uses web sockets for a connection

# How to use this branch

This part of the seminar involves installing and getting started with django channels.

To get this running, simply run the  the following 

## Step 1: Install requirements.txt

`pip install -r requirements.txt`

## Step 2: Create databases

Create the databases and the initial migrations with the following command:
`python manage.py migrate`

## Step 3: Run server

And start the server with 

`python manage.py runserver`

You should now be able to go to localhost:8000/chat/ and chat with the bot
