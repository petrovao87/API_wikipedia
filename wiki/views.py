from django.shortcuts import render
from rest_framework import generics
from wiki.serializers import NewNote

# Create your views here.


class CreateNote(generics.CreateAPIView):
    serializer_class = NewNote
