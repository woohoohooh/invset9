from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    comments_enabled = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content[:50]

class Company(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    rating = models.FloatField()
    def __str__(self):
        return self.name

class Advantage(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='advantages')
    position = models.PositiveIntegerField()
    advantage = models.CharField(max_length=255)
    mark = models.BooleanField()
    count = models.IntegerField()
    class Meta:
        ordering = ['position']
    def __str__(self):
        return self.advantage

class Position(models.Model):
    # Другие поля модели Position
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.BooleanField()
    comment = models.TextField()

class Review(models.Model):
    company = models.ForeignKey(Company, related_name='reviews', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rating = models.BooleanField()
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
