from django.urls import path 
from . import views

urlpatterns = [
    
    path('', views.index , name='home'),
    path('crop-image', views.cropImage , name='crop_image'),
    path('upload-image', views.uploadImage, name='upload_image'),

    path('upload/', views.upload_file, name='upload_file'),
    path('temp/', views.temp, name='temp'),
    path('temp1/', views.temp1, name='temp1'),

]
