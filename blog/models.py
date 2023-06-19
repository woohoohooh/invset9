from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    rating = models.FloatField(default=0)
    def __str__(self):
        return self.name

class SecurityScore(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    asset_secured_score = models.IntegerField(default=0)
    emission_limit_score = models.IntegerField(default=0)
    liquidity_score = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)

class TeamScore(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    decentralized_score = models.IntegerField(default=0)
    performace_score = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)

class ProductScore(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    performace_score = models.IntegerField(default=0)
    apy_1yr_score = models.IntegerField(default=0)
    apy_5yr_score = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)

class Guides(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    comments_enabled = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content[:50]

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
