from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('about/', views.About.as_view(),name = 'about'),
    path('',views.PostListView.as_view(),name = 'post_list'),
    path('post/<pk>/',views.PostDetailView.as_view(), name = 'post_detail'),
    path('post/',views.CreatePostView.as_view(), name = 'post_new'),
    path('post/edit/<pk>/',views.UpdatePostView.as_view(), name = 'post_edit'),
    path('post/delete/<pk>/', views.DeletePostView.as_view(), name = 'post_delete'),
    path('draft/', views.DraftListView.as_view(), name = 'post_draft'),
    path('comment/<pk>/', views.add_comment_to_post, name = 'comment'),
    path('comment/<pk>/approve/',views.comment_approve,name = 'comment_approve'),
    path('comment/<pk>/delete/',views.comment_delete, name = 'comment_delete'),
    path('post/<pk>/publish/',views.post_publish,name = 'post_publish')

]
