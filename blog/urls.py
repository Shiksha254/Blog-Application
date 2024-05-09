from django.urls import path
from. import views
from .views import HomeView,ArticleDetailView,AddPostView,UpdatePostView,DeletePostView,LikeView,AddCommentView
urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(),name='article_details'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(),name='update_post'),
    path('article/remove/<int:pk>', DeletePostView.as_view(),name='delete_post'),
    path('like/<int:pk>',LikeView,name='like_post'),
    path('add_post/', AddPostView.as_view(),name='add_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(),name='add_comment'),
    path('login/', views.login_user,name='login'),
    path('logout/', views.logout_user,name='logout'),
    path('register/', views.register_user,name='register'),
   
]
