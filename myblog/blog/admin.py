from django.contrib import admin
from .models import Post, Comment, Company, Advantage, Review

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Company)
admin.site.register(Advantage)
admin.site.register(Review)
