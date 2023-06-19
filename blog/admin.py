from django.contrib import admin
from .models import Post, Comment, Company, Advantage, Review, Guides, About, SecurityScore, TeamScore, ProductScore, Advantage, Category
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
    fields = ['asset_secured_score', 'emission_limit_score', 'liquidity_score']

class TeamcoreInline(admin.TabularInline):
    model = TeamScore
    extra = 1
    fields = ['decentralized_score', 'performace_score']

class ProductcoreInline(admin.TabularInline):
    model = ProductScore
    extra = 1
    fields = ['performace_score', 'apy_1yr_score', 'apy_5yr_score']

class AdvantageInline(admin.TabularInline):
    model = Advantage
    extra = 1

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [SecurityScoreInline, TeamcoreInline, ProductcoreInline, AdvantageInline]

admin.site.register(Post, fields=('title', 'content', 'category'))
admin.site.register(Comment)
admin.site.register(Advantage)
admin.site.register(Review)
admin.site.register(Guides)
admin.site.register(About)
admin.site.register(SecurityScore, SecurityScoreAdmin)
admin.site.register(TeamScore)
admin.site.register(ProductScore)
admin.site.register(Category)
