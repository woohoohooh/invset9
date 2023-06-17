from django.contrib import admin
from .models import Post, Comment, Company, Advantage, Review, Guides, About, SecurityScore, TeamScore, ProductScore
from django import forms

class SecurityScoreAdminForm(forms.ModelForm):
    class Meta:
        model = SecurityScore
        exclude = ('total_score',)

class SecurityScoreAdmin(admin.ModelAdmin):
    form = SecurityScoreAdminForm

class SecurityScoreInline(admin.StackedInline):
    model = SecurityScore
    extra = 1
    max_num = 1
    fields = ['field1', 'field2', 'field3']

class TeamcoreInline(admin.TabularInline):
    model = TeamScore
    extra = 1

class ProductcoreInline(admin.TabularInline):
    model = ProductScore
    extra = 1

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [SecurityScoreInline, TeamcoreInline, ProductcoreInline]

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Advantage)
admin.site.register(Review)
admin.site.register(Guides)
admin.site.register(About)
admin.site.register(SecurityScore, SecurityScoreAdmin)
admin.site.register(TeamScore)
admin.site.register(ProductScore)
