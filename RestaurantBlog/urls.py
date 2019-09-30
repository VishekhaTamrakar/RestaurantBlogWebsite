from django.conf.urls import url
from . import views
from django.urls import path,re_path
from . import views as RestaurantBlog_views
from django.contrib.auth import views as auth_views
app_name = 'RestaurantBlog'
urlpatterns = [

    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('restaurant_list', views.restaurant_list, name='restaurant_list'),
    path('restaurant/<int:pk>/edit/', views.restaurant_edit, name='restaurant_edit'),
    path('restaurant/<int:pk>/delete/', views.restaurant_delete, name='restaurant_delete'),
    path('restaurant/new/', views.restaurant_new, name='restaurant_new'),
    path('dish_list', views.dish_list, name='dish_list'),
    path('dish/new/', views.dish_new, name='dish_new'),
    path('dish/<int:pk>/edit/', views.dish_edit, name='dish_edit'),
    path('dish/<int:pk>/delete/', views.dish_delete, name='dish_delete'),
    path('review_list', views.review_list, name='review_list'),
    path('review/new/', views.review_new, name='review_new'),
    path('review/<int:pk>/edit/', views.review_edit, name='review_edit'),
    path('review/<int:pk>/delete/', views.review_delete, name='review_delete'),
    url(r'^signup/$', RestaurantBlog_views.signup, name='signup'),



]
