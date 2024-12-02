from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
# To force refresh
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.cache import add_never_cache_headers

from .forms import CustomUserCreationForm
from .models import Chat

import os
import json
import google.generativeai as genai

genai.configure(api_key="AIzaSyDm8-wHQ142JBXN54AgD3tv_gELp-1WxUw")


# Create your views here.
@login_required
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chat')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def userLogin(request):
    return render(request, 'login')

    # data = json.loads(request.body)
    # username = data["username"]
    # password = data["password"]
    # if request.method == "POST":
    #     user = authenticate(username=username, password=password)
    #     if user:
    #         login(request, user)
    #         return JsonResponse({'message': 'Login successful'})
    # return JsonResponse({'error': 'Invalid credentials'})


def userLogout(request):
    logout(request)
    response = HttpResponseRedirect(reverse("home"))
    add_never_cache_headers(response)
    return redirect('home')


@login_required
def chatWithBot(request):
    # Call the Gemini AI model here with user_message
    generation_config = genai.GenerationConfig(
        temperature=1,
        top_p=0.95,
        top_k=40,
        max_output_tokens=2000,
        response_mime_type="text/plain",
    )
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(history=[])
    response = None

    if request.method == "POST":
        user_message = request.POST.get("message")
        response = f"You said: {user_message}"  # Simple echo response
        try:
            response = chat_session.send_message(
                user_message)._result.candidates[0].content.parts[0].text

            chat_record = Chat(
                message=user_message,
                response=response
            )
            chat_record.save()  # Save the record to the database
        except KeyError as e:
            return JsonResponse({'error': f'Gemini API error: {str(e)}'}, status=500)
        except Exception as e:
            return JsonResponse({'error': f'An error occured: {str(e)}'})

    return render(request, "chat.html", {"response": response})


# def chatHistory(request):
#     # if request.user.is_authenticated:
#     chats = Chat.objects.filter(user=request.user).order_by('-timestamp')
#     history = [{
#         'message': chat.message,
#         'response': chat.response,
#         'timestamp': chat.timestamp
#     } for chat in chats]
#     return JsonResponse({'chat_history': history})
#     # return JsonResponse({'error': 'Unauthorized'}, status=401)

@login_required
def chatHistory(request):
    chats = Chat.objects.all().order_by('-timestamp')
    return render(request, "history.html", {"chats": chats})

@never_cache
def home(request):
    response = render(request, 'home.html', {'user': request.user})
    response['Cache-Control'] = 'no-store'
    return response
