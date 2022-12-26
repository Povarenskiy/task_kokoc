from django.urls import path
from questionnaire.views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>', TestView.as_view(), name='test'),
    path('<int:pk>/questions/', QuestionsView.as_view(), name='questions'),
    path('<int:pk>/questions/completed/', ComplitedView.as_view(), name='completed'),
    
]