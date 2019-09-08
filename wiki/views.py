from django.shortcuts import render
from rest_framework import generics, status
from wiki.serializers import NewNote, NoteList
from wiki.models import Note
import wikipedia
import requests
import json

from wiki.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.


class CreateNoteView(generics.CreateAPIView):
    # def post(self, request):
    #     data = request.data
    #     return data

    serializer_class = NewNote

    def create(self, request, *args, **kwargs):
        # print(request.data)
        # print(request.query_params)
        url = request.data['url']
        title = request.data['title']
        print(url, title)
        try:
            w = wikipedia.WikipediaPage(title)
            content = w.content
            categories = w.categories
            links = w.links
            images = w.images
            # return self.create(request, *args, **kwargs)
            data = json.dumps({'title': title, 'url': url, 'content': content, 'links': links, 'images': images}, )
            print(data)
            return self.create(url, title, content, categories, links, images, *args, **kwargs)
        except wikipedia.PageError:
            serializer = NewNote(data=request.data)
            return Response(status=status.HTTP_400_BAD_REQUEST)



class AllNoteView(generics.ListAPIView):
    serializer_class = NoteList
    queryset = Note.objects.all()
    permission_classes = (IsAuthenticated, )


class NoteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewNote
    queryset = Note.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)


