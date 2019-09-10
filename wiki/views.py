from django.shortcuts import render
from rest_framework import generics, status
from wiki.serializers import NewNote, NoteList, WikiSerializer
from wiki.models import Note
from wiki.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import wikipedia

# Create your views here.


class CreateNoteView(generics.CreateAPIView):
    serializer_class = NewNote

    def create(self, request, *args, **kwargs):
        url = request.data.get('url', None)
        title = request.data.get('title', None)
        serializer = NewNote(data={'url': url, 'title': title})

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            w = wikipedia.WikipediaPage(title)
            content = w.content
            categories = str(w.categories)
            links = str(w.links)
            images = str(w.images)
            data = {'title': title,
                    'url': url,
                    'content': content,
                    'categories': categories,
                    'links': links,
                    'images': images}
            serializer = WikiSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data={'title': title,
                                      'url': url,
                                      'content': content,
                                      'categories': categories,
                                      'links': links,
                                      'images': images},
                                status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except wikipedia.PageError as e:
            return Response(data={title: str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except wikipedia.DisambiguationError as e:
            data = {f'{e.title} may refer to:': e.options}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class AllNoteView(generics.ListAPIView):
    serializer_class = NoteList
    queryset = Note.objects.all()
    # permission_classes = (IsAuthenticated, )


class NoteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewNote
    queryset = Note.objects.all()
    # permission_classes = (IsAuthenticated, )
    # permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)


