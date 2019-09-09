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


import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
# Create your views here.


class CreateNoteView(generics.CreateAPIView):
    # def post(self, request):
    #     data = request.data
    #     return data

    serializer_class = NewNote
    # queryset = Note.objects.all()

    # def post(self, request, *args, **kwargs):
    #     url = request.data.get('url', None)
    #     title = request.data.get('title', None)
    #     w = wikipedia.WikipediaPage(title)
    #     content = w.content
    #     categories = str(w.categories)
    #     links = str(w.links)
    #     images = str(w.images)
    #     data = json.dumps({'title': title,
    #                                'url': url,
    #                                'content': content,
    #                                'categories': categories,
    #                                'links': links,
    #                                'images': images})
    #     request['data'] = data
    #     # serializer = NewNote(data=data)
    #     # print(serializer.is_valid())
    #     # if serializer.is_valid():
    #     #     print('_____'*100)
    #     #     serializer.save()
    #     #     return Response('data')
    #     # return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    #
    #     return self.create(request, *args, **kwargs)
    #
    #
    def create(self, request, *args, **kwargs):
        # print(request.data)
        # print(request.data)
        # print(request.query_params)
        url = request.data.get('url', None)
        title = request.data.get('title', None)
        # print(url, title)
        try:
            w = wikipedia.WikipediaPage(title)
            content = w.content
            categories = str(w.categories)
            links = str(w.links)
            images = str(w.images)
            # print(type(content), type(categories), type(links), type(images))
            # return self.create(request, *args, **kwargs)
            data = json.dumps({'title': [title],
                               'url': [url],
                               'content': [content],
                               'categories': [categories],
                               'links': [links],
                               'images': [images]})
            # user = self.get_queryset()
            # serializer = NewNote(data={'title': title,
            #                            'url': url,
            #                            'content': content,
            #                            'categories': categories,
            #                            'links': links,
            #                            'images': images})
            # json = JSONRenderer().render(serializer.data)
            serializer = NewNote(data=data)
            # stream = io.BytesIO(data1)
            # data = JSONParser().parse(stream)
            # print(repr(serializer))
            # print(serializer.initial_data)
            # serializer = NewNote(data='data')
            # print(data)
            # user = self.get_object()
            print(serializer.is_valid())
            # serializer.save()
            if serializer.is_valid():
                print('_____'*100)
                serializer.save()
            #     return Response('data')
            # return self.create(url, title, content, categories, links, images, *args, **kwargs)
            # return Response(data={'data': data})
            return Response(data={'title': title, 'url': url, 'content': content, 'links': links, 'images': images},
                            status=status.HTTP_201_CREATED)
        except wikipedia.PageError:
            # serializer = NewNote(data=request.data)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class AllNoteView(generics.ListAPIView):
    serializer_class = NoteList
    queryset = Note.objects.all()
    permission_classes = (IsAuthenticated, )


class NoteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewNote
    queryset = Note.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)


