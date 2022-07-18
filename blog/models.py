from django.db import models
from django.conf import settings

class Tag(models.Model):
    value = models.TextField(max_length=100)

    def __str__(self):
        return self.value

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    title = models.TextField(max_length=100)
    slug = models.SlugField()
    summary = models.TextField(max_length=500)
    content = models.TextField() 
    """ Content
    For simplicity we’ll just be storing the actual blog content as HTML,
    so we don’t have to worry about doing any kind of conversion when displaying it,
    we’ll just render the content field verbatim. This is not the most secure approach,
    so it’s only advisable if you trust your authors not to add malicious HTML.
    If you’re building a site that will output user-supplied HTML, consider using
    something like Bleach to remove unsafe HTML.
    """
    tags = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self):
        return self.title