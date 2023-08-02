from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    # post views
    
    path('', views.home, name='home'),
    path('fees/', views.fees, name='fees'),
    path('blog/', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('blog/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('activity_domain_1', views.activity_domain_1, name='activity_domain_1'),
    path('activity_domain_2', views.activity_domain_2, name='activity_domain_2'),
    path('activity_domain_3', views.activity_domain_3, name='activity_domain_3'),
    path('activity_domain_4', views.activity_domain_4, name='activity_domain_4'),
    path('question-list/', views.question_list, name='question-list'),
    path('question-detail/<int:year>/<int:month>/<int:day>/<slug:post>/', views.question_detail, name='question_detail'),
    path('question-ask/', views.question_ask, name='question-ask'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('contact/', views.contact, name='contact'),
    
]
