from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from users.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from questionnaire.models import *
from userprofile.models import Profile


class HomeView(ListView):
    """Отображение списка тестов"""
    template_name = 'questionnaire/home.html'
    model = Test


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['register_form'] = UserCreationForm()
        context['login_form'] = AuthenticationForm()
        return context


class TestView(LoginRequiredMixin, View):
    """Отображение вопросов теста"""
    template_name = 'questionnaire/test.html'
    
    def get(self, request, pk):
        test = Test.objects.get(pk=pk)
        questions = test.question_set.all()
        profile = Profile.objects.filter(user=request.user, tests=test)
        
        if not profile:
            context = {
                'test': test,
                'questions': questions ,
            }
            return render(request, self.template_name, context)
        else:
            return redirect(reverse('completed', kwargs={'pk': pk}))

    def post(self, request, pk):
        user = request.user
        test = Test.objects.get(pk=pk)
        questions = test.question_set.all()

        id_list = [request.POST.get(str(question.id)) for question in questions]
        answers = Answer.objects.filter(pk__in=id_list)

        for answer in answers:
            UserAnswer.objects.create(user=user, answer=answer, question=answer.question, test=test)
        
        profile = Profile.objects.get(user=user)
        profile.reward += test.reward
        profile.tests.add(test)
        profile.save()

        return redirect(reverse('completed', kwargs={'pk': pk}))
            

class QuestionsView(LoginRequiredMixin, ListView):
    template_name = 'questionnaire/question.html'
    model = Question

    def get_queryset(self, **kwargs):
        object_list = Question.objects.filter(test_id=self.kwargs['pk'])
        return object_list
    
 


class ComplitedView(LoginRequiredMixin, DetailView):
    template_name = 'questionnaire/completed.html'
    model = Test
        





