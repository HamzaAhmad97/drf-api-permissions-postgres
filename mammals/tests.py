from django.test import TestCase
from django.contrib.auth.models import User

from .models import Mammal


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(
            username="testuser1", 
            password="abc123")
        testuser1.save()

        # Create a Mammal
        test_mammal = Mammal.objects.create(
            added_by=testuser1, 
            name="some mammal", 
            scientific_name="scientific name",
            population = 1
        )
        test_mammal.save()

    def test_blog_content(self):
        mammal = Mammal.objects.get(id=1)
        expected_added_by = f"{mammal.added_by}"
        expected_name = f"{mammal.name}"
        expected_scientific_name = f"{mammal.scientific_name}"
        expected_population = f"{mammal.population}"
        self.assertEqual(expected_added_by, "testuser1")
        self.assertEqual(expected_name, "some mammal")
        self.assertEqual(expected_scientific_name, "scientific name")
        self.assertEqual(expected_population, "1")