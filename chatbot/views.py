from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from .forms import CustomUserCreationForm
from .models import Chat

import os
import json
import google.generativeai as genai

genai.configure(api_key="AIzaSyDm8-wHQ142JBXN54AgD3tv_gELp-1WxUw")


# Create your views here.
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

            if request.user.is_authenticated:
                Chat.objects.create(user=request.user,
                                    message=user_message, response=response)

        except KeyError as e:
            return JsonResponse({'error': f'Gemini API error: {str(e)}'}, status=500)
        except Exception as e:
            return JsonResponse({'error': f'An error occured: {str(e)}'})

    return render(request, "chat.html", {"response": response})


@login_required
def chatHistory(request):
    if request.user.is_authenticated:
        chats = Chat.objects.filter(user=request.user).order_by('-timestamp')
        return render(request, "history.html", {"chats": chats})
    else:
        return redirect('login')


def home(request):
    return render(request, 'home.html')
