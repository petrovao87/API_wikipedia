from rest_framework import serializers
from wiki.models import Note


class NewNote(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'