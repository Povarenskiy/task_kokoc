from django.urls import path, include

from userprofile.views import *

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('list/', ProfileListView.as_view(), name='profilelist'),
]