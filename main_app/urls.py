from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('about/', views.about, name='about'),
    path('blog/<int:blog_id>/', views.blog_detail, name='detail'),
    path('blog/create/', views.BlogCreate.as_view(), name='blog_create'),
    path('blog/', views.blog_index, name='blog'),

    path('blog/<int:pk>/update', views.BlogUpdate.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete', views.BlogDelete.as_view(), name='blog_delete'),
    # path('blog/<int:blog_id>/add_comment', views.add_comment, name='add_comment'),
    # path('blog/<int:blog_id>/unused_tags/<int:tag_id>/', views.unused_tag,  name='unused_tag'),
    # path('tag/create/', views.TagCreate.as_view(), name='tag_create'),
    # path('tag/', views.tag_index, name='tag'),  
    # path('tag/<int:tag_id>/', views.tag_detail, name='tag_detail'),
    # path('blog/<int:blog_id>/add_tag', views.add_tag, name='add_tag'),
    
]