"""
URL configuration for MeetingProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from Project.views.home_view import home_view
from Project.views.view_meeting import edit_meeting, meetings_view, invitations_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('meetings/', meetings_view, name='meeting'),
    path('meetings/edit/<int:meeting_id>/', edit_meeting, name='edit_meeting'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('invitations/', invitations_view, name='invitations'),

]
