import random
from django.conf import settings
from django.db import models
from django.db.models import Q, lookups
from django.utils.text import slugify 
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from meals.utils import generate_meal_queue_totals
from meals.models import (meal_added, meal_removed)

User = settings.AUTH_USER_MODEL

class ArticleQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == '':
            return self.none()
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookups)


class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)

class Article(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)

    objects = ArticleManager()

    @property
    def name(self):
        return self.title


    def get_asolute_url(self):
        # return f'/articles/{self.slug}/'
        return reverse('articles:detail', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        super().save(*args, **kwargs)

def slugify_instance_title(instance, save=False, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    qs = Article.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        # auto generating new slug
        rand_int = random.randint(300_000, 500_000)
        slug = f'{slug}-{rand_int}'
        return slugify_instance_title(instance, save=save, new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance

def article_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance)

pre_save.connect(article_pre_save, sender=Article)



def article_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)
        
post_save.connect(article_post_save, sender=Article)


def meal_added_rec(sender, instance, *args, **kwargs):
    # print('Addded', args, kwargs)
    user = instance.user
    data = generate_meal_queue_totals(user)
    print(data)

meal_added.connect(meal_added_rec)


def meal_removed_rec(*args, **kwargs):
    print('Removed', args, kwargs)

meal_removed.connect(meal_removed_rec)