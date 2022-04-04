from django.test import TestCase
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Article

class ArticleTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
        username='test',
        email='test@test.com',
        password='secret'
        )
        self.article = Article.objects.create(
            title='a title',
            body='Content',
            author=self.user
        )

    def test_article_delete_view(self):
        response = self.client.article(reverse('article_delete', args='1'))
        self.assertEqual(response.status_code, 302)