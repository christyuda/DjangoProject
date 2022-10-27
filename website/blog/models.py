from django.db import models
from django import forms
from django.db.models import Model, CharField, TextField


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    post = models.TextField()

    def __str__(self):
        return "{}".format(self.title)


class PostForm(forms.Form):
    title = forms.CharField(required=True, max_length=100)
    post = forms.CharField(required=True, min_length=9, widget=forms.Textarea)

    class Meta:
        model = Post
        field = ['title', 'post']