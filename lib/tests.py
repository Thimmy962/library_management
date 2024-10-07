
from django.test import TestCase, Client
from .models import Members, Reviews, Authors
from django.contrib.contenttypes.models import ContentType


# Create your tests here.
class CreateReviewsTest(TestCase):
    def setUp(self) -> None:
        

        member_user = Members.objects.create_user(email='ol@gmail.com', password='password', phone_number = "1234567890")
        member_user2 = Members.objects.create_user(email='gd@gmail.com', password='password', phone_number = "0987654321")

        author = Authors.objects.create(first_name = "Ted", last_name = "Dekker")
        author.save()

        authora = Authors.objects.create(first_name = "Dan", last_name = "Brown")
        authora.save()

        contentType = ContentType.objects.get(pk = 7)
        Reviews.objects.create(object_id = 1, content_type = contentType, comment = "What a lovely author",
                               reviewer = member_user, rating = 2)
        
        Reviews.objects.create(object_id = 1, content_type = contentType, comment = "What a lovely author",
                               reviewer = member_user2, rating = 2)

    def test_author_name(self):
        a = Authors.objects.get(pk = 2)
        review2 = Reviews.objects.get(pk = 2)
        model = review2.content_type.model_class()
        a1 = model.objects.get(pk = 2)
        self.assertEqual(a.first_name, "Dan")
        
        self.assertNotEqual(a, a1)

    def test_booKs(self):
        c = Client()
        response = c.get("/books")
        self.assertNotEqual(response.status_code, 200)

    def test_author_list(self):
        authors = Authors.objects.all()
        auta = Authors.objects.get(pk = 2)
        self.assertEqual(authors[1], auta)

    def test_authors(self):
        author = Authors.objects.all()
        self.assertEquals(author.count(), 2)