from django.test import TestCase
from wiki.models import Note

# Create your tests here.

class NoteModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Note.objects.create(title='gRPC',
                            url='https://en.wikipedia.org/wiki/GRPC',
                            content='gRPC is an open source remote procedure call (RPC)',
                            categories='Google software',
                            links='Microservices',
                            images='images_links')

    def test_title_label(self):
        note = Note.objects.get(id=1)
        field_label = note._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_url_label(self):
        note = Note.objects.get(id=1)
        field_label = note._meta.get_field('url').verbose_name
        self.assertEquals(field_label, 'url')

    def test_object_name_is_title_coma_url(self):
        note = Note.objects.get(id=1)
        expected_object_name = f'{note.title}, {note.url}'
        self.assertEquals(expected_object_name, str(note))
