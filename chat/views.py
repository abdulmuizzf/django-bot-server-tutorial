from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login as session_login, logout as session_logout

import random

def login(request):
    """
    Authenticates and logs the user in if username is not already in use
    """
    context={
        'error': None
    }
    if request.method=='POST':
        username = request.POST.get('username','')
        print(request.POST)
        user = authenticate(request, username=username)
        
        if user:
            if user.active == True:
                context['error'] = f"Username '{username}' is already taken. Please try another one."
                return render(request, 'chat/login.html', context)
            
            user.active = True
            user.save()
            session_login(request, user)
            return redirect(request.GET.get("next", reverse('chat')))

    return render(request, 'chat/login.html', context)

@login_required
def chat(request):
    return render(request, 'chat/chatbot.html')

def logout(request):
    request.user.active = False
    request.user.save()
    session_logout(request)
    return HttpResponseRedirect(reverse('login'))
    
def respond_to_websockets(message):
    jokes = {
     'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
     'fat':    ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
     'dumb':   ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
                """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""] 
     }  

    result_message = {
        'type': 'text'
    }
    if 'fat' in message['text']:
        result_message['text'] = random.choice(jokes['fat'])
    
    elif 'stupid' in message['text']:
        result_message['text'] = random.choice(jokes['stupid'])
    
    elif 'dumb' in message['text']:
        result_message['text'] = random.choice(jokes['dumb'])

    elif message['text'] in ['hi', 'hey', 'hello']:
        result_message['text'] = "Hello to you too! If you're interested in yo mama jokes, just tell me fat, stupid or dumb and i'll tell you an appropriate joke."
    else:
        result_message['text'] = "I don't know any responses for that. If you're interested in yo mama jokes tell me fat, stupid or dumb."

    return result_message