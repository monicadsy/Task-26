from django.test import TestCase
from django.urls import reverse
from .models import Stickynote


# Create your tests here.
class StickynoteModelTest(TestCase):
    def setUp(self):
        # Create a Stickynote object for testing
        Stickynote.objects.create(name='Test Stickynote', description='This is a test stickynote')

    def test_stickynote_has_name(self):
        # Test that a stickynote objet has the expepcted name
        stickynote = Stickynote.objects.get(id=1)
        self.assertEqual(stickynote.name, 'Test Stickynote')
    
    def test_stickynote_has_description(self):
        # Test that a stickynote objet has the expepcted description
        stickynote = Stickynote.objects.get(id=1)
        self.assertEqual(stickynote.description, 'This is a test stickynote.')


class StickynoteViewTest(TestCase):
    def setUp(self):
        # Create a Stickynote object for testing views
        Stickynote.objects.create(name='Test Stickynote', description='This is a test stickynote.')

    def test_stickynote_list_view(self):
        # Test the stickynote-list view
        response = self.client.get(reverse('stickynote_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Stickynote')

    def test_stickynote_detail_view(self):
        # Test the stickynote-detail view
        stickynote = Stickynote.objects.get(id=1)
        response = self.client.get(reverse('stickynote_detail', args=[str(stickynote.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Stickynote')
        self.assertContains(response, 'This is a test stickynote.')
