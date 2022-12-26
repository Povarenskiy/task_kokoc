from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from users.models import User
from userprofile.models import *
from questionnaire.models import Test, UserAnswer


class ProfileView(LoginRequiredMixin, View):
    template_name = 'userprofile/profile.html'

   
    def get(self, request, **kwargs):
        profile, created = Profile.objects.get_or_create(user=request.user)
        return render(request, self.template_name, {'profile': profile})


    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        context = {'profile': profile}

        border_color = request.POST.get('border-color')
        background_color = request.POST.get('background-color')
        
        if border_color:
            context = self.change_border_color(border_color, context)
                
        if background_color:
            context = self.change_background_color(background_color, context)
       
        return render(request, self.template_name, context)  


    def change_background_color(self, new_color, context):
        price = 300
        
        profile = context.get('profile')
        result = profile.reward - price
        if result >= 0:
            profile.background_color = new_color
            profile.reward = result
            profile.save()
        else:
            context['background_error'] = 'Недостаточно очков на смену фона. Нужно больше тестов!'
        return context 


    def change_border_color(self, new_color, context):
        price = 150

        profile = context.get('profile')
        result = profile.reward - price
        if result >= 0:
            profile.border_color = new_color
            profile.reward = result
            profile.save()
        else:
            context['border_error'] = 'Недостаточно очков на смену рамки. Нужно больше тестов!'
        return context 


class ProfileListView(ListView):
    template_name = 'userprofile/profilelist.html'
    model = Profile
    
