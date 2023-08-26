"""
URL configuration for todo_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from tasks.views import all_list_view, list_tasks_view, task_view

urlpatterns = [
    path('list/', all_list_view),
    path('list/<slug:slug>/', list_tasks_view, name='list_all_tasks'),
    path('list/<slug:list_slug>/<int:pk>', task_view, name='task_details'),
]
