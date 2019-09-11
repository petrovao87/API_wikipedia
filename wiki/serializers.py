from rest_framework import serializers
from wiki.models import Note


class NewNote(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Note
        # fields = '__all__'
        fields = ('title', 'url')


class NoteList(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'url')


class WikiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('title', 'url', 'content', 'categories', 'links', 'images')
