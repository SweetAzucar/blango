from django.contrib import admin

from blog.models import Tag, Post

MODELS = [Tag, Post]

for model in MODELS:
  admin.site.register(model)

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
