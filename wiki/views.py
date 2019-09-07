from django.shortcuts import render
from rest_framework import generics
from wiki.serializers import NewNote, NoteList
from wiki.models import Note

# Create your views here.


class CreateNoteView(generics.CreateAPIView):
    serializer_class = NewNote


class AllNoteView(generics.ListAPIView):
    serializer_class = NoteList
    queryset = Note.objects.all()


class NoteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewNote
    queryset = Note.objects.all()


