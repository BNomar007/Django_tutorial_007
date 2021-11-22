from django.test import TestCase

from .models import Article
from django.utils.text import slugify 

class ArticleTestCase(TestCase):
    def setUp(self):  # create a new database content for database test
        self.num_of_articles = 5
        for i in range(0, self.num_of_articles):
            Article.objects.create(title='Hello World', content='new content')

    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(), self.num_of_articles)

    def test_hello_world_slug(self):
        obj = Article.objects.all().order_by('id').first()
        title = obj.title
        slug = obj.slug
        slug_title = slugify(title)
        self.assertEqual(slug, slug_title)

    def test_unique_slug(self):
        ps = Article.objects.exclude(slug__iexact='hello-world')
        for obj in qs:
            title = obj.title
            slug = obj.slug
            slug_title = slugify(title)
            self.assertNotEqual(slug, slug_title)



