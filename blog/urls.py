from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('guides/', views.guides, name='guides'),
    path('about/', views.about, name='about'),
    path('', views.post_list, name='post_list'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('companies/', views.company_ratings, name='company_ratings'),
    path('companies/<int:company_id>/', views.company_detail, name='company_detail'),
    path('companies/<int:company_id>/add-advantage/', views.add_advantage, name='add_advantage'),
    path('advantages/<int:advantage_id>/increment/', views.increment_advantage, name='increment_advantage'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
