from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Catagory(models.Model):
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.description


class Article(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    catagory = models.ForeignKey(
        Catagory,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.id])
