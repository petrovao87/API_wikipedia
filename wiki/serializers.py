from rest_framework import serializers
from wiki.models import Note


class NewNote(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Note
        fields = '__all__'


class NoteList(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'url', 'user')
