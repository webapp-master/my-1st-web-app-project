from django.urls import path
from . import views
from .views import search_record, lab_test, css_flex


urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('search_record/', search_record, name='search_record'),
    path('lab/', lab_test, name='Labouratory'),
    path('flex/', css_flex, name='flex_c'),
    path('dashboard/', views.dashboard_page, name='dash_page'),


]