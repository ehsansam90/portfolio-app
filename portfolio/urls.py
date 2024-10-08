"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page route
    path('resume/', views.resume, name='resume'), # Resume page route
    path('new-page/', views.new_page, name='new_page'),
    path('send_message/', views.send_message, name='send_message'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('survey/', views.survey, name='survey'),
    path('survey/thank-you/', views.survey_thank_you, name='survey_thank_you'),

]

# urlpatterns += static(setting.MEDIA_URL, document_root=setting.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

