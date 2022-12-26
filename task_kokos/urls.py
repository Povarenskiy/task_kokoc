from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('_nested_admin/', include('nested_admin.urls')),
    path('', include('questionnaire.urls')),
    path('user/', include('users.urls')),
    path('profile/', include('userprofile.urls'))
]
