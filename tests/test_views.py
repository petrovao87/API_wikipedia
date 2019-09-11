from django.test import TestCase
from wiki.models import Note
from django.urls import reverse

# Create your tests here.


class AuthorListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 10 authors for pagination tests
        number_of_notes = 10
        for note_num in range(number_of_notes):
            Note.objects.create(title=str(note_num), url=str(note_num), )

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/api/v0/wiki/note/all/')
        print(resp)
        self.assertEqual(resp.status_code, 200)


