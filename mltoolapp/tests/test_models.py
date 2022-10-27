from django.test import TestCase

# Create your tests here.

from mltoolapp.models import MLDiagram

class MLDiagramModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        MLDiagram.objects.create(name='New Test diagram')

    def test_slug_label(self):
        mldiagram = MLDiagram.objects.get(id=1)
        self.assertEqual(mldiagram.slug, 'new-test-diagram')

   
    def test_name_max_length(self):
        mldiagram = MLDiagram.objects.get(id=1)
        max_length = mldiagram._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

  
    def test_get_absolute_url(self):
        mldiagram = MLDiagram.objects.get(id=1)
        print('ML:  ', mldiagram)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(mldiagram.get_absolute_url(), '/mltoolapp/mldiagam/new-test-diagram/')
