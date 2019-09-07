from django.shortcuts import render
from rest_framework import generics
from wiki.serializers import NewNote, NoteList
from wiki.models import Note
import wikipedia

from wiki.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class CreateNoteView(generics.CreateAPIView):

    serializer_class = NewNote


class AllNoteView(generics.ListAPIView):
    serializer_class = NoteList
    queryset = Note.objects.all()
    permission_classes = (IsAuthenticated, )


class NoteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewNote
    queryset = Note.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )


