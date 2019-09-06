from django.contrib import admin
from django.urls import path, include
from wiki.views import CreateNote


app_name = 'note'
urlpatterns = [
    path('note/create/', CreateNote.as_view())
]